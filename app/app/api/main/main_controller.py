from flask import Blueprint
from flask.app import Flask
from app.api import response


routes = Blueprint('main', __name__, url_prefix='/')


@routes.route('', methods=['GET'])
def index():
    return response.success("App is running correctly")


def register_routes(flask_app: Flask):
    flask_app.register_blueprint(routes)
