#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main entry point for the Skin Prick Test Reporting application.
"""

import os
import sys
import json
import logging
import logging.config
from PyQt5 import QtWidgets
from config import settings
from app.ui.main_controller import MainWindow


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
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "json",
                "filename": settings.LOG_DIR + "/spt_reporting.log",
                "mode": "a",
                "maxBytes": 1024 * 1024 * 10,  # 10 MB,
                "backupCount": 10,
                "encoding": "utf8",
            },
        },
        "root": {"level": settings.LOG_LEVEL, "handlers": ["default", "file"]},
    }

    logging.config.dictConfig(log_config_dict)
    logger = logging.getLogger(__name__)
    return logger


def ensure_dir_exists(path):
    """
    Checks that a specified directory is present and has write permissions.
    If it does not exist, attempts to create it.
    """
    try:
        os.makedirs(path, exist_ok=True)
    except PermissionError:
        logger.error(f"Cannot create directory at {path}. Check permissions.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error while creating directory at {path}: {e}")
        sys.exit(1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    ensure_dir_exists(settings.LOG_DIR)
    ensure_dir_exists(settings.DATA_DIR)
    ensure_dir_exists(settings.REPORT_DIR)
    logger = configure_logging()
    logger.debug("Logging configured")
    main()
