from flask import Blueprint, request
from app.helpers import response, signup
from ..users.model import UserModel
from ..account.model import AccountModel
from ..address.model import AddressModel


routes = Blueprint('main', __name__)

@routes.route('/')
def index():
  return response.success("App is running correctly")

@routes.route('/signup/', methods=['POST'])
@response.handleExceptions
def signup_route():
  body = request.get_json(force=True)

  user = address = account = None

  try:
    user = body['user']
  except Exception as e:
    print(e)
    return response.error('user field cannot be empty', status=400)
  
  try:
    address = body['address']
  except Exception as e:
    print(e)
    return response.error('address field cannot be empty', status=400)
    
  try:
    account = body['account']
  except:
    print(e)
    return response.error('account field cannot be empty', status=400)

  try:
    result = signup.register(user, address, account)
    return response.success(result)
  except ValueError as e:
    print(e)
    return response.error(e, status=400)
  except Exception as e:
    raise e
