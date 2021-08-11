from dataclasses import asdict
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from app.api import response
from app.infra.db.daos.recipe import RecipeRatingDao
from app.app import recipe_finding_usecase, authentication_use_case, user_finding_usecase


routes = Blueprint('users', __name__, url_prefix='/users')
recipeRatingDao = RecipeRatingDao()


@routes.route('/<int:user_id>', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_user(user_id):
    data = user_finding_usecase.find_by_id(user_id)
    return response.success(data)


@routes.route('/<int:user_id>/recipes', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_user_recipes(user_id):
    recipes = recipe_finding_usecase.find_all(user_id=user_id)
    return response.success(list(map(asdict, recipes)))


@routes.route('/<int:user_id>/likes', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_user_liked_recipes(user_id):
    recipes = recipe_finding_usecase.find_all_liked_by(user_id)

    return response.success(list(map(asdict, recipes)))


@routes.route('/<int:user_id>/ratings', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_user_ratings(user_id):
    authentication_use_case.ensure_same_user(user_id, current_identity.id)

    data = recipeRatingDao.getRatingsByUser(user_id)
    return response.success(data)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
