from flask import Blueprint, request
from flask import Flask
from flask_jwt import jwt_required
from src.api import response
from src.infra.db.daos.ingredient import IngredientDao, QuantityUnitDao

routes = Blueprint('ingredients', __name__, url_prefix='/ingredients')
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_ingredients():
    populated_ingredients = []
    ingredients = []

    search_name = request.args.get('name')
    if search_name:
        ingredients = ingredientDao.getIngredientsByName(search_name)
    else:
        ingredients = ingredientDao.getAll()

    for ingredient in ingredients:
        quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
        quantity = str.format('{} {}', int(
            ingredient.baseQuantity), quantity_unit.abbreviation)
        populated_ingredients.append({
            'id': ingredient.id,
            'name': ingredient.name,
            'quantity': quantity,
            'price': ingredient.baseCost
        })
    return response.success(populated_ingredients)


@routes.route('/<int:ingredient_id>/mesures', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_ingredient_mesures(ingredient_id):
    quantityUnits = quantityUnitDao.getAllQuantityUnitsByIngredientId(ingredient_id)
    return response.success(quantityUnits)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
