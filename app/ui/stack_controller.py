import logging
from PyQt5.QtWidgets import QStackedWidget

logger = logging.getLogger(__name__)


class StackController:
    def __init__(self, stacked_widget: QStackedWidget):
        self._stacked_widget = stacked_widget
        self._stack_map = {stacked_widget.widget(i).objectName(): i for i in range(stacked_widget.count())}
        self.current_state = stacked_widget.currentWidget().objectName()
        try:
            if self._stack_map["p_main"]:
                self.current_state = "p_main"
        except KeyError:
            logger.error("No main page found in stack map")
        logger.info(f"Stack map created: {self._stack_map}")

    @property
    def current_state(self):
        # return the current state of the stacked widget as a string
        return self._stacked_widget.currentWidget().objectName()

    @current_state.setter
    def current_state(self, widget_name):
        if widget_name not in self._stack_map:
            raise ValueError(f"Widget name {widget_name} not found in stack map")
        self._current_state = self._stack_map[widget_name]
        self._stacked_widget.setCurrentIndex(self._current_state)
