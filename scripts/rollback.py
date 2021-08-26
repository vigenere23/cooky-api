from yoyo import read_migrations, get_backend
from yoyo.scripts.main import configure_logging
import os
import time
from src.config import config

user = 'root'
password = config['database.root-password']
database = config['database.database']
host = config['database.host']
port = config['database.port']
current_dir = os.path.dirname(os.path.abspath(__file__))


def connect(n_tries: int = 10, timeout: int = 5):
    remaining_tries = n_tries
    timeout = 5

    while remaining_tries > 0:
        try:
            backend = get_backend(f'mysql://{user}:{password}@{host}:{port}/{database}')
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
    migrations_path = os.path.join(current_dir, '..', 'migrations')

    if not os.path.isdir(migrations_path):
        raise RuntimeError(f"No migrations directory found at path '{migrations_path}'")

    migrations = read_migrations(migrations_path)
    backend = connect()

    print('Rollbacking migrations...')
    configure_logging(2)

    with backend.lock():
        backend.rollback_migrations(backend.to_rollback(migrations))

    print('DONE!')


if __name__ == '__main__':
    main()
