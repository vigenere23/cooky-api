from flask import Blueprint, request
from flask_jwt import jwt_required, current_identity
from app.helpers import response
from .dao import UserDao
from .model import UserModel
from ..recipe.dao import RecipeDao
from ..likeRecipe.dao import LikeRecipeDao
from ..carts.dao import CartDao
from ..commands.dao import CommandDao
from ..account.model import AccountModel
from ..account.dao import AccountDao
from ..address.dao import AddressDao
from ..address.model import AddressModel
from ..rating.dao import RatingDao

routes = Blueprint('users', __name__)
userDao = UserDao()
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
cartDao = CartDao()
commandDao = CommandDao()
accountDao = AccountDao()
addressDao = AddressDao()
ratingDao = RatingDao()

@routes.route('/', methods=['GET'])
@jwt_required()
@response.handleExceptions
def index():
  return response.success(userDao.getAll())

@routes.route('/<int:id>/account', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAccount(id):
  response.ensureIdentity(id, current_identity)

  account = accountDao.getAccountByUserId(id)
  del account.password
  address = addressDao.getById(account.id_Address)
  return response.success({
    **account.serialize(),
    'address': address.serialize()
  })

@routes.route('/<int:id>/email/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyEmail(id):
  response.ensureIdentity(id, current_identity)

  body = request.get_json(force=True)
  try:
    result = accountDao.modifyEmail(body['email'], id) 
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/password/', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyPassword(id):
  response.ensureIdentity(id, current_identity)

  body = request.get_json(force=True)
  try:
    accountDao.modifyPassword(body['password'], id)
    return response.success('')
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/country', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyCountry(id):
  response.ensureIdentity(id, current_identity)

  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyCountry(body['country'], addressId)
  return response.success(data)

@routes.route('/<int:id>/city', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyCity(id):
  if not response.ensureIdentity(id, current_identity):
    return response.error('Access forbidden', status=401)

  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyCity(body['city'], addressId)
  return response.success(data)

@routes.route('/<int:id>/street', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyStreet(id):
  response.ensureIdentity(id, current_identity)

  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyStreet(body['street'], addressId)
  return response.success(data)

@routes.route('/<int:id>/apartment', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyApartment(id):
  response.ensureIdentity(id, current_identity)

  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyApartment(body['apartment'], addressId)
  return response.success(data)

@routes.route('/<int:id>/doorNumber', methods=['PUT'])
@jwt_required()
@response.handleExceptions
def modifyDoorNumber(id):
  response.ensureIdentity(id, current_identity)

  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyDoorNumber(body['number'], addressId)
  return response.success(data)

@routes.route('/<int:id>', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getOne(id):
  data = userDao.getById(id)
  return response.success(data)


@routes.route('/<int:id>/recipes', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAllRecipesByUser(id):
  data = recipeDao.getAllRecipesByUser(id)
  return response.success(data)

@routes.route('/<int:id>/likes', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getLikeRecipes(id):
  recipes = []
  likes = likeRecipeDao.getLikeRecipeByUser(id)
  for like in likes:
    recipe = recipeDao.getById(like.id_Recipe)
    recipes.append({
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description
    })

  return response.success(recipes)

@routes.route('/<int:id>/ratings', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getRatings(id):
  response.ensureIdentity(id, current_identity)

  data = ratingDao.getRatingsByUser(id)
  return response.success(data)

@routes.route('/<int:id>/cart', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getUserCart(id):
  response.ensureIdentity(id, current_identity)

  data = cartDao.getCurrentUserCart(id)
  return response.success(data)

@routes.route('/<int:id>/commands', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getUserCommands(id):
  response.ensureIdentity(id, current_identity)

  commands = commandDao.getUserCommands(id)
  data = []
  for command in commands:
    cart = cartDao.getById(command.id_Cart)
    data.append({
      **command.serialize(),
      'totalCost': cart.totalCost
    })
  return response.success(data)

@routes.route('/<int:id>/address', methods=['GET'])
@jwt_required()
@response.handleExceptions
def getAddress(id):
  response.ensureIdentity(id, current_identity)

  userData = accountDao.getAccountByUserId(id)
  address = userData.id_Address
  return response.success(addressDao.getAddress(address))
