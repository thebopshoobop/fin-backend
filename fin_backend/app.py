from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    from fin_backend.models import db
    db.init_app(app)
    db.create_all(app=app)

    from fin_backend.api.hello import hello
    app.register_blueprint(hello, url_prefix="/api")

    return app
