import os
import click
from flask.cli import FlaskGroup


def create_fin_app(info):
    from fin_backend.app import create_app
    return create_app("")
    # create_app(config=os.environ.get('WIKI_CONFIG', 'wikiconfig.py'))


@click.group(cls=FlaskGroup, create_app=create_fin_app)
def cli():
    """This is a management script for the feedfin backend."""


if __name__ == '__main__':
    cli()
