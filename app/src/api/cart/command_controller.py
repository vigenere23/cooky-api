from dataclasses import asdict
from datetime import datetime
from flask import Blueprint
from flask.app import Flask
from flask_jwt import jwt_required, current_identity
from src.api import response
from src.infra.db.daos.cart import CartDao, CommandDao
from src.infra.db.models.cart import CommandModel


routes = Blueprint('commands', __name__, url_prefix='/user/commands')
cartDao = CartDao()
commandDao = CommandDao()


@routes.route('', methods=['GET'])
@jwt_required()
@response.handleExceptions
def get_current_user_commands():
    commands = commandDao.getUserCommands(current_identity.id)
    data = []
    for command in commands:
        cart = cartDao.getById(command.id_Cart)
        data.append({
            **asdict(command),
            'totalCost': cart.totalCost
        })
    return response.success(data)


@routes.route('', methods=['POST'])
@jwt_required()
@response.handleExceptions
def create_current_user_command():
    cart = cartDao.get_cart_of(current_identity.id)

    commandModel = CommandModel(
        id_Cart=cart.id,
        creationDate=datetime.now()
    )
    result = commandDao.save(commandModel)

    return response.success(result)


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
