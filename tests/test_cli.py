# pylint: disable=missing-docstring,redefined-outer-name
"""Ensure that the CLI behaves itself."""
import subprocess
import pathlib
import unittest.mock
import re

import pytest
from click.testing import CliRunner

from fin_backend.manage import cli


@pytest.fixture
def runner():
    return CliRunner()


class TestDoc:
    """Ensure that the documentation runner works properly."""

    def test_default(self, runner, monkeypatch):
        mock_run = unittest.mock.MagicMock()
        monkeypatch.setattr(subprocess, "run", mock_run)
        result = runner.invoke(cli, ["doc"])
        assert result.exit_code == 0
        assert mock_run.call_count == 1
        attrs = mock_run.call_args[0][0]
        assert len(attrs) == 3
        assert sum(map(lambda a: pathlib.Path(a).exists(), attrs)) == 3

    def test_custom_venv(self, runner, monkeypatch):
        mock_run = unittest.mock.MagicMock()
        monkeypatch.setattr(subprocess, "run", mock_run)
        result = runner.invoke(cli, ["-e", "potatoes", "doc"])
        assert result.exit_code == 0
        assert re.match(r"Unable to find.*", result.output)
        assert mock_run.call_count == 0


class TestTest:
    """Ensure that the test runner works properly."""

    def test_default(self, runner, monkeypatch):
        mock_run = unittest.mock.MagicMock()
        monkeypatch.setattr(subprocess, "run", mock_run)
        result = runner.invoke(cli, ["test"])
        assert result.exit_code == 0
        assert mock_run.call_count == 1
        attrs = mock_run.call_args[0][0]
        assert len(attrs) == 1
        assert pathlib.Path(attrs[0]).exists()

    def test_custom_venv(self, runner, monkeypatch):
        mock_run = unittest.mock.MagicMock()
        monkeypatch.setattr(subprocess, "run", mock_run)
        result = runner.invoke(cli, ["-e", "potatoes", "test"])
        assert result.exit_code == 0
        assert re.match(r"Unable to find.*", result.output)
        assert mock_run.call_count == 0
