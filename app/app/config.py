import os
from datetime import timedelta
from dataclasses import dataclass


@dataclass
class FlaskConfig:
    SECRET_KEY: str
    JWT_AUTH_URL_RULE: str
    JWT_EXPIRATION_DELTA: timedelta


@dataclass
class DatabaseConfig:
    user: str
    password: str
    host: str
    port: str
    database: str
    connection_timeout: int
    use_pure: bool


@dataclass
class Config:
    flask: FlaskConfig
    database: DatabaseConfig


config = Config(
    flask=FlaskConfig(
        SECRET_KEY = os.getenv('SECRET_KEY', 'some-secret'),
        JWT_AUTH_URL_RULE = '/login',
        JWT_EXPIRATION_DELTA = timedelta(minutes=30)
    ),
    database=DatabaseConfig(
        user='api',
        password=os.getenv('MYSQL_PASSWORD', 'api'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '8082'),
        database='projet',
        connection_timeout=5,
        use_pure=True
    )
)
