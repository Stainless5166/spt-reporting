from PyQt5 import QtWidgets, uic


class YourMainWindowClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/ui/main.ui", self)
        self.setWindowTitle("SPT - Reporting")
        self.apply_actions_to_buttons()
        self.back_stack = []

    def start_program(self):
        self.show()
        self.stack_controller("Home")
        return True

    def apply_actions_to_buttons(self):
        buttons = self.findChildren(QtWidgets.QPushButton)
        for button in buttons:
            button.clicked.connect(self.button_controller)

    def button_controller(self):
        print("Button pressed" + self.sender().objectName())

    # This is the function that controls the stack of the
    # main window as a state machine.
    def stack_controller(self, stack: str):
        # map stack to index
        stack_map = {
            "Home": 0,
            "StartTest": 1,
            "RecordResults": 2,
            "Save": 3,
            "Print": 4,
        }
        self.stackedWidget.setCurrentIndex(stack_map[stack])

    def stop_program(self):
        self.hide()
        return True
