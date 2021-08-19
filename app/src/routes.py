from flask import Flask
from flask_cors import CORS
from src.context import logger
from src.api.main import main_controller
from src.api import auth
from src.api.ingredient import ingredients_controller
from src.api.recipe import recipes_controller
from src.api.cart import cart_controller, command_controller
from src.api.user import user_controller, users_controller, account_controller, accounts_controller


def print_route_infos(routes_map):
    route_infos = "\n*** ROUTES ***\n"
    registered_routes = sorted(
        routes_map.iter_rules(),
        key=lambda rule: rule.rule
    )
    for route in registered_routes:
        methods = ','.join(filter(lambda m: m not in ('HEAD', 'OPTIONS'), route.methods))
        padding = ' ' * (16 - len(methods))
        url = route.rule
        handler = route.endpoint
        route_infos += f"  {methods}{padding}{url}  ->  {handler}\n"

    logger.info(route_infos)


def initialize_routes(flask_app: Flask):
    main_controller.register_routes(flask_app)
    ingredients_controller.register_routes(flask_app)
    cart_controller.register_routes(flask_app)
    command_controller.register_routes(flask_app)
    recipes_controller.register_routes(flask_app)
    user_controller.register_routes(flask_app)
    users_controller.register_routes(flask_app)
    account_controller.register_routes(flask_app)
    accounts_controller.register_routes(flask_app)
    auth.register_routes(flask_app)

    CORS(flask_app)
