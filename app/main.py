from PyQt5 import QtWidgets

from PyQt5 import QtWidgets


class YourMainWindowClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")

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
