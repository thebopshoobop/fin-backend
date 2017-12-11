"""Command line interface
=========================
"""

import subprocess
import pathlib

import click
import flask.cli

from fin_backend.app import create_app
from fin_backend.config import DevelopmentConfig
from fin_backend.models import db


def _create_fin_app(flask_script_info):  # pylint: disable=unused-argument
    return create_app(DevelopmentConfig())


def _get_current_path():
    current = pathlib.Path(__file__).parent
    return current


def _path_exists(path, path_name=""):
    path_name = path_name if path_name else path
    exists = pathlib.Path(path).exists()
    if not exists:
        click.echo(
            f"Unable to find {path_name}. Have you built your virtualenv?")

    return exists


@click.group(cls=flask.cli.FlaskGroup, create_app=_create_fin_app)
@click.option("--env", "-e", default="venv",
              help="Custom virtualenv directory. Defaults to `venv`.")
@click.pass_context
def cli(ctx, env):
    """This is a management script for the feedfin backend."""
    ctx.obj.data['env'] = env


@cli.command()
@click.pass_context
def doc(ctx):
    """Builds the Sphinx HTML docs."""
    current = _get_current_path()
    sphinx_build = current.joinpath(ctx.obj.data['env'], 'bin/sphinx-build')
    source_dir = current.joinpath('docs/source')
    build_dir = current.joinpath('docs/build')

    if _path_exists(sphinx_build, "sphinx_build"):
        subprocess.run([sphinx_build, source_dir, build_dir])


@cli.command()
@click.pass_context
def test(ctx):
    """Runs the test suite."""
    current = _get_current_path()
    pytest = current.joinpath(ctx.obj.data['env'], 'bin/pytest')

    if _path_exists(pytest, "pytest"):
        subprocess.run([pytest])


@cli.command()
@click.pass_context
def wipe(ctx):
    """Resets the database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
