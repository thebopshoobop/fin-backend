from secrets import token_urlsafe

from envparse import env

env.read_envfile()


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        database = env.str('DATABASE_URL', default="sqlite:///:memory:")
        self.SQLALCHEMY_DATABASE_URI = database

        secret_key = env.str('SECRET_KEY', default=token_urlsafe())
        self.SECRET_KEY = secret_key


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
