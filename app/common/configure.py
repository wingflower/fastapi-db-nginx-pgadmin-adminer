import sys

from os import path
from yaml import safe_load
from collections import namedtuple
from app.common import consts


base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


def nestednamedtuple(dictionary: dict) -> namedtuple:
    if isinstance(dictionary, Mapping) and not isinstance(dictionary, fdict):
        for key, value in list(dictionary.items()):
            dictionary[key] = nestednamedtuple(value)
        return namedtuple("namedtupled", dictionary)(**dictionary)
    elif isinstance(dictionary, list):
        return [nestednamedtuple(item) for item in dictionary]

    return dictionary


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


@singleton
class Config:
    def __init__(self, global_name="global_config"):
        self.global_name = f"{global_name}"
        self.data = self._set_config()

    def _set_config(self):
        try:
            if consts.API_ENV.lower() == "local":
                return consts.local_config()
            else:
                return consts.prod_config()
            # config_file = path.join(base_dir, 'app/common/consts.yml')
            # with open(config_file) as f:
            #     ENV = safe_load(f)
            #     if ENV.get("API_ENV", "local").lower() == "local":
            #         CONF = ENV.get("LOCAL_CONFIG")
            #     else:
            #         CONF = ENV.get("PROD_CONFIG")
            # return CONF
        except Exception as e:
            print(e)
            return {}
