from flask import Blueprint, request, json
from app.helpers import response, exceptions, queries
from datetime import datetime
from ..cartItem.model import CartItemModel
from .dao import CartDao
from ..cartItem.dao import CartItemDao
from ..commands.dao import CommandDao
from ..commands.model import CommandModel
from ..ingredient.dao import IngredientDao
from ..quantityUnit.dao import QuantityUnitDao

routes = Blueprint('carts', __name__)
cartDao = CartDao()
cartItemDao = CartItemDao()
commandsDao = CommandDao()
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(cartDao.getAll())

@routes.route('/<int:id>')
@response.handleExceptions
def getCart(id):
  return response.success(cartDao.getById(id))

@routes.route('/<int:id>/items')
@response.handleExceptions
def getCartItems(id):
  cartItems = cartItemDao.getItemsByCart(id)
  data = []
  for cartItem in cartItems:
    ingredient = ingredientDao.getById(cartItem.id_Ingredient)
    quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
    quantity = str.format('{} {}', int(ingredient.baseQuantity), quantity_unit.abbreviation)
    data.append({
      **cartItem.serialize(),
      'name': ingredient.name,
      'baseCost': ingredient.baseCost,
      'quantity': quantity
    })
  return response.success(data)

@routes.route('/<int:id>/items/', methods=['POST'])
@response.handleExceptions
def addItemToCart(id):
  body = request.get_json(force=True)
  data = {
    'id_Ingredient': body['id_Ingredient'],
    'id_Cart': id,
    'multiplier': '1'
  }
  cartItemModel = CartItemModel(**data)
  result = cartItemDao.save(cartItemModel)
  return response.success(result)

@routes.route('/<int:id_Cart>/items/<int:id_Ingredient>/', methods=['DELETE'])
@response.handleExceptions
def deleteItemFromCart(id_Cart, id_Ingredient):
  cartItemDao.deleteIngredient(id_Cart, id_Ingredient)
  return response.success("", status=204)

@routes.route('/<int:id_Cart>/items/<int:id_Ingredient>/', methods=['PUT'])
@response.handleExceptions
def modifyRecipeName(id_Cart, id_Ingredient):
  body = request.get_json(force=True)
  result = cartItemDao.modifyQuantity(body['multiplier'], id_Cart, id_Ingredient)
  return response.success(result)


@routes.route('/<int:id>/command', methods=['GET'])
@response.handleExceptions
def getCommandsByCart(id):
  data = commandsDao.getCommandByCart(id)
  if (data):
    return response.success(data)
  else:
    return response.error("This cart is not in command")


@routes.route('/<int:id>/command/', methods=['POST'])
@response.handleExceptions
def createCommand(id):
  data = {
    'id_Cart': id,
    'creationDate': datetime.now()
  }
  commandModel = CommandModel(**data)
  data = commandsDao.save(commandModel)
  return response.success(data)
