import sys
import os
import logging
from PyQt5 import QtWidgets
from app.ui.main_controller import YourMainWindowClass

from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    settings_files=['settings.toml', '.secrets.toml']
)

logger_path = settings.LOG_FILE
logger_dir = os.path.dirname(logger_path)
if not os.path.exists(logger_dir):
    os.makedirs(logger_dir)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    handlers=[
        logging.FileHandler(settings.LOG_FILE),
        logging.StreamHandler()
    ]
)
# create logger
logger = logging.getLogger(__name__)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YourMainWindowClass()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
