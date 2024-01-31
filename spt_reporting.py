import sys
import json
import logging
import logging.config
from PyQt5 import QtWidgets
from dynaconf import Dynaconf
from app.ui.main_controller import MainWindow

SETTINGS = Dynaconf(
    environments=True,
    settings_files=["settings.json"],
)


class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
        }
        return json.dumps(data)


def configure_logging():
    log_config_dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {"()": JsonFormatter},
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "json",
                "filename": SETTINGS.LOG_FILE,
                "mode": "a",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["default", "file"]},
    }

    logging.config.dictConfig(log_config_dict)
    logger = logging.getLogger(__name__)
    return logger


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    logger = configure_logging()
    logger.debug("Logging configured")
    main()
