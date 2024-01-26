import sys
import logging
import logging.config
from PyQt5 import QtWidgets
from dynaconf import Dynaconf

SETTINGS = Dynaconf(
    environments=True,
    settings_files=['settings.json'],
)


def configure_logging():
    log_config_dict = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'stream': 'ext://sys.stdout',
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': SETTINGS.LOG_FILE,
                'mode': 'a',
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['default', 'file']
        }
    }

    logging.config.dictConfig(log_config_dict)
    logger = logging.getLogger(__name__)
    return logger


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = app.ui.main_controller.YourMainWindowClass()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    configure_logging()
    main()
