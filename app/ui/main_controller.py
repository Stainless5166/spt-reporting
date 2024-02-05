import os

from PyQt5 import QtWidgets, uic
import logging
from dynaconf import settings
from app.ui.stack_controller import StackController
from app.patient import Patient

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.patients = None
        uic.loadUi("app/ui/main_controller.ui", self)
        self.setWindowTitle("SPT - Reporting")
        self.apply_actions_to_buttons()
        self.stack_controller = StackController(self.stackedWidget)
        self.load_patients_for_selector()

    def start_program(self):
        self.show()
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

    def load_patients_for_selector(self):
        # this method will be used to load the patients for the patient selector from the SETTINGS.DATA_DIR
        # first pull filenames from the directory SETTINGS.DATA_DIR
        # then create a list of patients from the filenames
        self.patients = []
        filenames = os.listdir(settings.DATA_DIR)
        for file in filenames:
            self.patients.append(Patient(file))
        # then populate the patient selector with the list of patients names
        self.patient_selector.clear()
        for patient in self.patients:
            self.patient_selector.addItem(patient.person.name)
