from dotenv import load_dotenv
load_dotenv()

from yoyo import read_migrations, get_backend
from yoyo.scripts.main import configure_logging
import os
import time

user = 'root'
password = os.getenv('MYSQL_ROOT_PASSWORD')
database = 'projet'
url = 'localhost:8082'
current_dir = os.path.dirname(os.path.abspath(__file__))


def connect(n_tries: int = 10, timeout: int = 5):
    remaining_tries = n_tries
    timeout = 5

    while remaining_tries > 0:
        try:
            backend = get_backend(f'mysql://{user}:{password}@{url}/{database}')
            print('Successfully connected to database')
            return backend
        except Exception as e:
            remaining_tries -= 1
            print('Database connection failed.')
            print(e)

            if remaining_tries <= 0: break

            print(f'Retrying in {timeout} seconds')
            time.sleep(timeout)


def main():
    backend = connect()
    migrations = read_migrations(os.path.join(current_dir, '..', '..', 'migrations'))

    print('Rollbacking migrations... (this can take a long time)')
    configure_logging(2)

    with backend.lock():
        backend.rollback_migrations(backend.to_rollback(migrations))

    print('DONE!')


if __name__ == '__main__':
    main()
