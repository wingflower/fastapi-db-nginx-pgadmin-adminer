import sys

from os import path
from yaml import safe_load
from dataclasses import dataclass


base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


try:
    with open('./consts.yml') as f:
        ENV = safe_load(f)
except:
    sys.exit()

print(ENV)


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class Config:
    BASE_DIR = base_dir
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@singleton
@dataclass
class LocalConfig(Config):
    DB_URL: str = "mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8mb4".format_map(ENV)
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


@singleton
@dataclass
class ProdConfig(Config):
    DB_URL: str = "mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8mb4".format_map(ENV)
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


def conf():
    if ENV.get("API_ENV", "local") == "local":
        return LocalConfig()
    else:
        return ProdConfig()


if __name__ == '__main__':
    CFG = conf()
    print(CFG.__dict__)
