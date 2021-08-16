from dotenv import load_dotenv
load_dotenv()

from yoyo import read_migrations
from yoyo import get_backend
import os

user = 'root'
password = os.getenv('MYSQL_ROOT_PASSWORD')
database = 'projet'
url = 'localhost:8082'
current_dir = os.path.dirname(os.path.abspath(__file__))

backend = get_backend(f'mysql://{user}:{password}@{url}/{database}')
migrations = read_migrations(os.path.join(current_dir, '..', 'migrations'))

with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))
