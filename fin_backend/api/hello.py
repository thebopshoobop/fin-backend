from flask import Blueprint
from fin_backend.models import db, User

hello = Blueprint("hello", __name__)


@hello.route("/", defaults={"name": "World"})
@hello.route("/<name>")
def show(name):
    if name != "World":
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    return f"Hello, {name}!"


@hello.route("/users")
def shows():
    users = User.query.all()
    return ', '.join([user.name for user in users])
