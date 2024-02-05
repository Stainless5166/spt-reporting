from app.ui.stack_controller import StackController
from PyQt5.QtWidgets import QStackedWidget, QWidget
import pytest


@pytest.fixture(scope="module")
def qt_stacked_widget():
    # this is a test instance of the QStackedWidget
    # for testing purposes, it contains 3 named widgets
    # that contain labels
    test_stacked_widget = QStackedWidget()
    for name in ["State_0", "State_1", "State_2"]:
        widget = QWidget()
        widget.setObjectName(name)
        test_stacked_widget.addWidget(widget)

    yield test_stacked_widget  # This is where the testing happens!


class TestStackController:
    @pytest.fixture(autouse=True)
    def setup_test_stack_controller_for_testing(self, qt_stacked_widget):
        self.stack_controller = StackController(qt_stacked_widget)

    def test_set_state(self):
        self.stack_controller.current_state = "State_0"
        assert self.stack_controller.current_state == "State_0", "State for 'State_0' should be `State_0`"

    def test_get_state(self):
        self.stack_controller.current_state = "State_2"
        assert self.stack_controller.current_state == "State_2", "State for 'State_2' should be `State_2`"
