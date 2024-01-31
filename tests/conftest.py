# conftest.py
import pytest
import logging
import logging.config
import json
from dynaconf import Dynaconf


class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps(record.__dict__)


LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "()": JsonFormatter,
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "json"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}


@pytest.fixture(autouse=True, scope="session")
def set_up_logging():
    """Fixture to set up logging for each test."""
    logging.config.dictConfig(LOGGING_CONFIG)


@pytest.fixture(autouse=True, scope="session")
def set_up_settings():
    """Fixture to set up settings for each test."""
    SETTINGS = Dynaconf(
        environments=True,
        settings_files=["settings.toml"],
    )
    return SETTINGS
