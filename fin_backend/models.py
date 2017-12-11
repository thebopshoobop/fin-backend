"""Model definitions."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    # username = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    # password_hash = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


# class Feed(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     url = db.Column(db.String(240), nullable=False)
#     etag = db.Column(db.String(80))
#     modified = db.Column(db.String(80))


# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     feed = db.Column(Feed, nullable=False)
#     author = db.Column(db.String(80))
#     title = db.Column(db.String(120))
#     url = db.Column(db.String(240), nullable=False)
#     read = db.Column(db.Boolean)
#     published = db.Column(db.Datetime)
#     summary = db.Column(db.String(512))
#     image = db.Column(db.string(120))


# class Category(db.Model):
#     title = db.Column(db.String(120))
