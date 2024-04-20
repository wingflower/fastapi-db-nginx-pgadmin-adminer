from dataclasses import dataclass
from os import path, environ


# ENV = dotenv_values(find_dotenv())
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    DB_USER = "test"
    DB_PASSWD = "test"
    DB_ADDR = "mariadb"
    DB_PORT = 3306
    DB_NAME = "test"
    DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    JWT_SECRET = "test"
    JWT_ALGORITHM = "HS256"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    ALLOW_METHODS = ["*"]
    ALLOW_HEADERS = ["*"]
    EXCEPT_PATH_LIST= [
        "/",
        "/openapi.json"
    ]
    EXCEPT_PATH_REGEX = "^(/docs|/redoc|/api/auth)"
    MAX_API_KEY = 3
    MAX_API_WHITELIST = 10


@dataclass
class ProdConfig(Config):
    DB_USER = "test"
    DB_PASSWD = "test"
    DB_ADDR = "mariadb"
    DB_PORT = 3306
    DB_NAME = "test"
    DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    JWT_SECRET = "test"
    JWT_ALGORITHM = "HS256"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    ALLOW_METHODS = ["*"]
    ALLOW_HEADERS = ["*"]
    EXCEPT_PATH_LIST= [
        "/",
        "/openapi.json"
    ]
    EXCEPT_PATH_REGEX = "^(/docs|/redoc|/api/auth)"
    MAX_API_KEY = 3
    MAX_API_WHITELIST = 10


def conf():
    config = dict(prod=ProdConfig(), local=LocalConfig())
    # return config.get(ENV.get("API_ENV", "local").lower())
    return config.get(environ.get("API_ENV", "local").lower())
