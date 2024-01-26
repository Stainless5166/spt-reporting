import logging

from PyQt5.QtWidgets import QStackedWidget


class StackController:
    def __init__(self, stacked_widget: QStackedWidget):
        self._stack_map = {
            stacked_widget.widget(i).objectName(): i
            for i in range(stacked_widget.count())
        }
        self._current_state = stacked_widget.currentIndex()
        logging.info(f'Stack map created: {self._stack_map}')

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, widget_name: str):
        self._current_state = self._stack_map[widget_name]
