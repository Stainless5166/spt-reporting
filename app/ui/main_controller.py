from PyQt5 import QtWidgets, uic
import logging

from app.ui.stack_controller import StackController

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app/ui/main_controller.ui", self)
        self.setWindowTitle("SPT - Reporting")
        self.apply_actions_to_buttons()
        self.stack_controller = StackController(self.stackedWidget)

    def start_program(self):
        self.show()
        self.stack_controller.current_state = "Home"
        # Following line is used to mimic the functionality of
        # `self.stackedWidget.setCurrentIndex(stack_map[stack])` statement
        # from the previous `stack_controller` method.
        self.stackedWidget.setCurrentIndex(self.stack_controller.current_state)
        return True

    def apply_actions_to_buttons(self):
        buttons = self.findChildren(QtWidgets.QPushButton)
        for button in buttons:
            button.clicked.connect(self.button_controller)

    def button_controller(self):
        print("Button pressed" + self.sender().objectName())

    def stop_program(self):
        self.hide()
        return True
