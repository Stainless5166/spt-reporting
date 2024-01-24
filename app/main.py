import sys
from PyQt5 import QtWidgets
from app.ui.main_controller import YourMainWindowClass

from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    settings_files=['settings.toml', '.secrets.toml']
)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YourMainWindowClass()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
