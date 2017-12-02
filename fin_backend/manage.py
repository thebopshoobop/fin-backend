import click
from flask.cli import FlaskGroup

from fin_backend.app import create_app
from fin_backend.config import DevelopmentConfig


def create_fin_app(info):
    return create_app(DevelopmentConfig())


@click.group(cls=FlaskGroup, create_app=create_fin_app)
def cli():
    """This is a management script for the feedfin backend."""


if __name__ == "__main__":
    cli()
