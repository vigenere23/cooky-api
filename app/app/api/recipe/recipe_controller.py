from dataclasses import asdict
from flask import Blueprint, request
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.api.recipe.recipe_creation_request import RecipeCreationRequest
from app.api.recipe.recipe_edition_requests import CommentCreationRequest, RatingCreationRequest, RecipeEditionRequest
from app.api.requests import parse_body
from app.application.recipe.recipe_edition_dto import RecipeEditionDto
from app.application.recipe.recipe_creation_dto import RecipeCreationDto
from app.infra.db.daos.recipe import RecipeIngredientDao, LikeRecipeDao, RecipeRatingDao, RecipeCommentDao
from app.infra.db.models.recipe import LikeRecipeModel, RatingModel, CommentModel
from app.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao
from app.app import recipe_creation_usecase, recipe_finding_usecase, recipe_editing_usecase, authentication_use_case, user_finding_usecase

routes = Blueprint('recipes', __name__, url_prefix='/recipes')
like_recipe_dao = LikeRecipeDao()
comment_dao = RecipeCommentDao()
recipe_rating_dao = RecipeRatingDao()
recipe_ingredient_dao = RecipeIngredientDao()
ingredient_dao = IngredientDao()
quantity_unit_dao = QuantityUnitDao()


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def index():
    recipes = recipe_finding_usecase.find_all(
        name=request.args.get('name')
    )

    return response.success(list(map(asdict, recipes)))


@routes.route('', methods=['POST'])
@jwt_required()
@response.handleExceptions
@parse_body(RecipeCreationRequest)
def addRecipe(request_data: RecipeCreationRequest):
    recipe_creation_dto = RecipeCreationDto(recipe={
        'id_User': current_identity.id,
        'name': request_data.name,
        'description': request_data.description,
        'directives': request_data.directives
    }, ingredients=request_data.ingredients)
    recipe = recipe_creation_usecase.create_recipe(recipe_creation_dto)

    return response.success(asdict(recipe))


@routes.route('/<int:recipe_id>', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getRecipeById(recipe_id):
    recipe = recipe_finding_usecase.find_by_id(recipe_id)
    user = user_finding_usecase.find_by_id(recipe.id_User)
    data = {
        **asdict(recipe),
        'user': {
            **asdict(user)
        }
    }
    return response.success(data)


@routes.route('/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
@response.handleExceptions
def deleteRecipe(recipe_id):
    recipe_editing_usecase.delete_recipe(current_identity.id, recipe_id)
    return response.empty()


@routes.route('/<int:recipe_id>/name', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(RecipeEditionRequest)
def modifyRecipeName(request_data: RecipeEditionRequest, recipe_id):
    edition_dto = RecipeEditionDto(id=recipe_id, name=request_data.name)
    modified_recipe = recipe_editing_usecase.edit_recipe(current_identity.id, edition_dto)

    return response.success(asdict(modified_recipe))


@routes.route('/<int:recipe_id>/directives', methods=['PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(RecipeEditionRequest)
def modifyRecipeDirective(request_data: RecipeEditionRequest, recipe_id):
    edition_dto = RecipeEditionDto(id=recipe_id, name=request_data.directives)
    modified_recipe = recipe_editing_usecase.edit_recipe(current_identity.id, edition_dto)

    return response.success(asdict(modified_recipe))


@routes.route('/<int:recipe_id>/ingredientQuantity', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyIngredientQuantity(recipe_id):
    recipe = recipe_finding_usecase.find_by_id(recipe_id)

    authentication_use_case.ensure_same_user(recipe.id_User, current_identity.id)

    body = request.get_json(force=True)
    result = recipe_ingredient_dao.modifyQuantity(
        recipe_id, body['id_Ingredient'], body['totalQuantity'])
    return response.success(result)


@routes.route('/<int:recipe_id>/ingredients', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getIngredientsByRecipe(recipe_id):
    data = []
    recipeIngredients = recipe_ingredient_dao.getIngredientsByRecipe(recipe_id)
    for recipeIngredient in recipeIngredients:
        ingredient = ingredient_dao.getById(recipeIngredient.id_Ingredient)
        quantityUnit = quantity_unit_dao.getById(
            recipeIngredient.id_QuantityUnit)
        data.append({
            'id': ingredient.id,
            'name': ingredient.name,
            'quantityUnit': asdict(quantityUnit),
            'totalQuantity': recipeIngredient.totalQuantity
        })

    return response.success(data)


@routes.route('/<int:recipe_id>/comments')
@jwt_required()
@response.handleExceptions
def getRecipeComments(recipe_id):
    comments = comment_dao.getRecipeComments(recipe_id)
    data = []
    for comment in comments:
        user = user_finding_usecase.find_by_id(comment.id_User)
        data.append({
            **asdict(comment),
            'user': asdict(user)
        })
    return response.success(data)


@routes.route('/<int:recipe_id>/likes', methods=['POST', 'DELETE'])
@jwt_required()
@response.handleExceptions
def likeRecipe(recipe_id):
    likeRecipeModel = LikeRecipeModel(
        id_User=current_identity.id,
        id_Recipe=recipe_id
    )

    if request.method == 'POST':
        result = like_recipe_dao.save(likeRecipeModel)
        return response.success(result)
    else:
        like_recipe_dao.delete(likeRecipeModel)
        return response.empty()


@routes.route('/<int:recipe_id>/ratings', methods=['POST', 'PUT'])
@jwt_required()
@response.handleExceptions
@parse_body(RatingCreationRequest)
def addRateRecipe(request_data: RatingCreationRequest, recipe_id):
    ratingModel = RatingModel(
        id_User=current_identity.id,
        id_Recipe=recipe_id,
        value=request_data.value
    )

    if request.method == 'POST':
        result = recipe_rating_dao.save(ratingModel)
    else:
        result = recipe_rating_dao.replace(ratingModel)

    return response.success(result)


@routes.route('/<int:recipe_id>/comments', methods=['POST'])
@jwt_required()
@response.handleExceptions
@parse_body(CommentCreationRequest)
def addCommentRecipe(request_body: CommentCreationRequest, recipe_id):
    commentModel = CommentModel(
        id_User=current_identity.id,
        id_Recipe=recipe_id,
        text=request_body.text
    )
    result = comment_dao.save(commentModel)

    return response.success(result)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
