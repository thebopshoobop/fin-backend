"""
Command line interface
======================
"""

import subprocess
import pathlib

import click
import flask.cli

from fin_backend.app import create_app
from fin_backend.config import DevelopmentConfig


def _create_fin_app(flask_script_info):  # pylint: disable=unused-argument
    return create_app(DevelopmentConfig())


@click.group(cls=flask.cli.FlaskGroup, create_app=_create_fin_app)
@click.option("--env", "-e", default="venv",
              help="Custom virtualenv directory. Defaults to `./venv`.")
@click.pass_context
def cli(ctx, env):
    """This is a management script for the feedfin backend."""
    ctx.obj.data['env'] = env


@cli.command()
@click.pass_context
def doc(ctx):
    """Builds the fin-backend Sphinx HTML docs."""
    current = pathlib.Path(__file__).parent.parent
    current.resolve()

    sphinx_build = current.joinpath(ctx.obj.data['env'], 'bin/sphinx-build')
    source_dir = current.joinpath('docs/source')
    build_dir = current.joinpath('docs/build')

    if not pathlib.Path(sphinx_build).exists():
        print("Unable to find sphinx-build. Have you built your virtualenv?")
    else:
        subprocess.run([sphinx_build, source_dir, build_dir])


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
