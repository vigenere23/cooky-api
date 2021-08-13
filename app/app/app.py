from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from app.config import config
from app.routes import initialize_routes, print_route_infos


flask_app = Flask(__name__)
flask_app.config.from_object(config.flask)

initialize_routes(flask_app)
print_route_infos(flask_app.url_map)
