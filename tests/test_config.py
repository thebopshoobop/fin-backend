# pylint: disable=missing-docstring,redefined-outer-name,no-self-use
"""Ensure that the configuration classes are properly configured."""
import os

import pytest

import fin_backend.config as config


@pytest.fixture
def base():
    return config.Config


@pytest.fixture
def production():
    return config.ProductionConfig


@pytest.fixture
def testing():
    return config.TestingConfig


@pytest.fixture
def development():
    return config.DevelopmentConfig


@pytest.fixture
def environment():
    return {
        'FEEDFIN_DEBUG': "true",
        'FEEDFIN_TESTING': "true",
        'FEEDFIN_SECRET_KEY': "pineapples",
        'DATABASE_URL': "guavas",
        'DATABASE_TEST_URL': "guavas"
    }


class TestDefaults:
    """Ensure that the config classes set their defaults properly."""

    @pytest.mark.parametrize('config_class',
                             [base(), production(), testing(), development()])
    def test_core_defaults(self, config_class, monkeypatch):
        monkeypatch.setattr(os, "environ", {})
        instance = config_class()
        assert len(instance.SECRET_KEY) > 30 and str(instance.SECRET_KEY)
        assert instance.SQLALCHEMY_DATABASE_URI == 'sqlite:///:memory:'
        assert instance.SQLALCHEMY_TRACK_MODIFICATIONS is False

    @pytest.mark.parametrize('config_class', [base(), production()])
    def test_production_defaults(self, config_class, monkeypatch):
        monkeypatch.setattr(os, "environ", {})
        instance = config_class()
        assert instance.DEBUG is False
        assert instance.TESTING is False

    def test_test_defaults(self, testing, monkeypatch):
        monkeypatch.setattr(os, "environ", {})
        instance = testing()
        assert instance.DEBUG is False
        assert instance.TESTING is True

    def test_dev_defaults(self, development, monkeypatch):
        monkeypatch.setattr(os, "environ", {})
        instance = development()
        assert instance.DEBUG is True
        assert instance.TESTING is False


class TestConfigured:
    """Ensure that the config classes properly reflect environment vars."""

    @pytest.mark.parametrize('config_class',
                             [base(), production(), testing(), development()])
    def test_core_defaults(self, config_class, environment, monkeypatch):
        monkeypatch.setattr(os, "environ", environment)
        instance = config_class()
        assert instance.SECRET_KEY == "pineapples"
        assert instance.SQLALCHEMY_DATABASE_URI == "guavas"
        assert instance.SQLALCHEMY_TRACK_MODIFICATIONS is False
        assert instance.DEBUG is True
        assert instance.TESTING is True

    def test_test_defaults(self, testing, environment, monkeypatch):
        environment['DEBUG'] = False
        monkeypatch.setattr(os, "environ", environment)
        instance = testing()
        assert instance.DEBUG is True
        assert instance.TESTING is True

    def test_dev_defaults(self, development, environment, monkeypatch):
        environment['TESTING'] = False
        monkeypatch.setattr(os, "environ", {})
        instance = development()
        assert instance.DEBUG is True
        assert instance.TESTING is False
