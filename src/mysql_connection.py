import time
from mysql.connector import MySQLConnection
from src.config import config


def connect_to_mysql(n_tries: int = 10, timeout: int = 5) -> MySQLConnection:
    remaining_tries = n_tries

    while remaining_tries > 0:
        try:
            connection = MySQLConnection(
                host=config['database.host'],
                port=config['database.port'],
                database=config['database.database'],
                user=config['database.user'],
                password=config['database.password'],
                connection_timeout=5
            )
            print('Successfully connected to database')
            return connection
        except Exception as e:
            remaining_tries -= 1
            print('Database connection failed.')
            print(e)

            if remaining_tries <= 0: break

            print(f'Retrying in {timeout} seconds')
            time.sleep(timeout)

    if remaining_tries == 0:
        raise Exception(
            f'Could not connect to database after {n_tries} tries. Aborting.')
