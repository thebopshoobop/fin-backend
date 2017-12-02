from flask import Blueprint

hello = Blueprint("hello", __name__)


@hello.route("/", defaults={"name": "World"})
@hello.route("/<name>")
def show(name):
    return f"Hello, {name}!"
