import sys
from PyQt5 import QtWidgets, uic


def print_all_widgets(parent):
    for child in parent.children():
        print(child.objectName())
        print_all_widgets(child)


class YourMainWindowClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/ui/main.ui", self)
        self.setWindowTitle("My Application")
        print_all_widgets(self)

    def start_program(self):
        self.show()
        return True

    def stop_program(self):
        self.hide()
        return True


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YourMainWindowClass()
    window.start_program()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
