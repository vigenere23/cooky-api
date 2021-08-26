from flask import Flask
from datetime import timedelta
from src.config import config
from src.routes import initialize_routes, print_route_infos


flask_app = Flask(__name__)
flask_app.config.update(
    SECRET_KEY=config['flask.secret'],
    JWT_AUTH_URL_RULE='/login',
    JWT_EXPIRATION_DELTA=timedelta(minutes=config['flask.jwt.expiration-in-minutes'])
)

initialize_routes(flask_app)
print_route_infos(flask_app.url_map)
