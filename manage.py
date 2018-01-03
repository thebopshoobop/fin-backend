"""Command line interface
=========================
"""

import subprocess
import pathlib
import sys

import click
import flask.cli

from fin_backend.app import create_app
from fin_backend.config import DevelopmentConfig
from fin_backend.models import db


def _create_fin_app(flask_script_info):  # pylint: disable=unused-argument
    return create_app(DevelopmentConfig())


def _build_executable(bin_file):
    return pathlib.Path(sys.base_exec_prefix).joinpath(f"bin/{bin_file}")


def _execute(args):
    if not pathlib.Path(args[0]).exists():
        return click.echo(f"Unable to find {args[0]}.")

    subprocess.run(args)


@click.group(cls=flask.cli.FlaskGroup, create_app=_create_fin_app)
def cli():
    """This is a management script for the feedfin backend."""


@cli.command()
def doc():
    """Builds the Sphinx HTML docs."""
    # pylint: disable=no-member
    current = pathlib.Path(__file__).parent.resolve()
    source_dir = current.joinpath('docs/source')
    build_dir = current.joinpath('docs/build')
    sphinx_build = _build_executable('sphinx-build')
    _execute([sphinx_build, source_dir, build_dir])


@cli.command()
def test():
    """Runs the test suite."""
    pytest = _build_executable('pytest')
    _execute([pytest])


@cli.command()
def lint():
    """Runs the linter."""
    pylint = _build_executable('pylint')
    click.secho('Linting App', fg='blue', bold=True)
    _execute([pylint, 'fin_backend'])
    click.secho('Linting Tests', fg='blue', bold=True)
    _execute([pylint, 'tests'])


@cli.command()
def wipe():
    """Resets the database."""
    db.drop_all()
    db.create_all()
    db.session.commit()  # pylint: disable=no-member


if __name__ == "__main__":
    cli()
