"""App factory
==============
"""

from flask import Flask


def create_app(config):
    """Flask app factory function

    Instantiates a new Flask app, loads the database connection and registers
    blueprints.

    Arguments:
        config (:obj:`fin_backend.config.Config`): Config object.

    Returns:
        :obj:`flask.Flask`: Flask app instance.
    """

    app = Flask(__name__)
    app.config.from_object(config)

    from fin_backend.models import db
    db.init_app(app)
    db.create_all(app=app)

    from fin_backend.api.hello import hello
    app.register_blueprint(hello, url_prefix="/api")

    return app
