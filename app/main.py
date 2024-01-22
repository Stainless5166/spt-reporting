import sys
from PyQt5 import QtWidgets
from ui.main_controller import YourMainWindowClass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YourMainWindowClass()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
