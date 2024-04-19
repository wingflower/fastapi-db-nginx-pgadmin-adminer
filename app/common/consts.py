API_ENV= "local"

def local_config():
    config =  dict(
        DB_USER= "test",
        DB_PASSWD= "test",
        DB_ADDR= "mariadb",
        DB_PORT= 3306,
        DB_NAME= "test",
        JWT_SECRET= "test",
        JWT_ALGORITHM= "HS256",
        TRUSTED_HOSTS = ["*"],
        ALLOW_SITE = ["*"],
        ALLOW_METHODS = ["*"],
        ALLOW_HEADERS = ["*"],
        EXCEPT_PATH_LIST= [
            "/",
            "/openapi.json"
        ],
        EXCEPT_PATH_REGEX= "^(/docs|/redoc|/api/auth)",
        MAX_API_KEY= 3,
        MAX_API_WHITELIST= 10
    )
    config["DB_URL"]= "mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8mb4".format_map(config)
    return config


def prod_config():
    config =  dict(
        DB_USER= "test",
        DB_PASSWD= "test",
        DB_ADDR= "mariadb",
        DB_PORT= 3306,
        DB_NAME= "test",
        JWT_SECRET= "test",
        JWT_ALGORITHM= "HS256",
        TRUSTED_HOSTS = ["*"],
        ALLOW_SITE = ["*"],
        ALLOW_METHODS = ["*"],
        ALLOW_HEADERS = ["*"],
        EXCEPT_PATH_LIST= [
            "/",
            "/openapi.json"
        ],
        EXCEPT_PATH_REGEX= "^(/docs|/redoc|/api/auth)",
        MAX_API_KEY= 3,
        MAX_API_WHITELIST= 10
    )
    config["DB_URL"]= "mysql+pymysql://{DB_USER}:{DB_PASSWD}@{DB_ADDR}:{DB_PORT}/{DB_NAME}?charset=utf8mb4".format_map(config)
    return config
