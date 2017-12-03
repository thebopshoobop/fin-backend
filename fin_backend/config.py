"""
App configuration classes
=========================

These classes establish the configuration settings for running the app in
development, testing, and production mode. If you need to override them, you
can set the appropriate environment variables. For ease of development you may
store environment variables in a :file:`.env` file placed in the app hierarchy.

The classes in this module must be instantiated before passing them into the
`flask.Flask` application object.
"""

from secrets import token_urlsafe

from envparse import Env

Env.read_envfile()

# pylint: disable=too-few-public-methods


class Config(object):
    """Base config class. Use one of subclasses below to configure the app.

    Attributes:
        DEBUG (`bool`): Enable Flask's debugging mode. Defaults to `True`.
            Override with the :envvar:`FEEDFIN_DEBUG` environment variable.
        TESTING (`bool`): Enable Flask's testing mode. Defaults to `True`.
            Override with the :envvar:`FEEDFIN_TESTING` environment variable.
        SECRET_KEY (`str`): Flask session secret. If unset, a new random token
            is generated on app instantiation. Override with the
            :envvar:`FEEDFIN_SECRET_KEY` environment variable.
        SQLALCHEMY_DATABASE_URI (`str`): Database URI for SQLAlchemy.
            Defaults to `sqlite:///:memory:`. Override with the
            :envvar:`DATABASE_URL` environment variable.
        SQLALCHEMY_TRACK_MODIFICATIONS (`bool`): Disable Flask-
            SQLAlchemy's event system. Set to `False` and not configurable.
    """

    def __init__(self):
        config = Env(
            FEEDFIN_DEBUG=dict(default=False),
            FEEDFIN_TESTING=dict(default=False),
            FEEDFIN_SECRET_KEY=dict(default=token_urlsafe()),
            DATABASE_URL=dict(default='sqlite:///:memory:')
        )
        # pylint: disable=invalid-name
        self.DEBUG = config('FEEDFIN_DEBUG')
        self.TESTING = config('FEEDFIN_TESTING')
        self.SECRET_KEY = config('FEEDFIN_SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production configuration subclass. Uses default config."""
    pass


class DevelopmentConfig(Config):
    """Development configuration subclass.

    Enables Flask's debugging mode. Note
    that this will not enable reloading. If you need reloading, you must set
    the environment variable :envvar:`FLASK_DEBUG=1`.
    """

    def __init__(self):
        super().__init__()
        self.DEBUG = True


class TestingConfig(Config):
    """Testing configuration subclass. Enables Flask's testing mode."""

    def __init__(self):
        super().__init__()
        self.TESTING = True
