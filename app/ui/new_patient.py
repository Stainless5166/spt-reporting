import json

from PyQt5 import QtWidgets, uic
from app.patient import Patient, Person
from PyQt5.QtWidgets import QLineEdit, QSpinBox, QCheckBox, QMessageBox
from typing import Any, Dict
from pydantic import BaseModel, ValidationError
import typing


def get_widget_mapping(model: BaseModel) -> Dict[str, Any]:
    widget_mapping = {}

    for field_name, field_value in model.__annotations__.items():
        if field_value == str or field_value == typing.Optional[str]:
            widget = QLineEdit()
        elif field_value == int or field_value == typing.Optional[int]:
            widget = QSpinBox()
        elif field_value == bool or field_value == typing.Optional[bool]:
            widget = QCheckBox()
        else:
            raise ValueError(
                f"Unsupported field type "
                f"{field_value} "
                f"for field {field_name}"
            )

        widget_mapping[field_name] = widget

    return widget_mapping


class NewPatient(QtWidgets.QDialog):
    """
    This is the controller for the new patient dialog.

    This class is expected to load the following widgets
    from the corresponding .ui file:
    - back_button: QPushButton that triggers closing of the dialog
    - save_button: QPushButton that triggers saving the data
    entered in the form
    - field_list: QFormLayout that contains the fields
    for creating a new patient
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the NewPatient class
        :param args:
        :param kwargs:
        """
        super(NewPatient, self).__init__(*args, **kwargs)
        self.patient = Patient()
        self.ui = uic.loadUi("app/ui/new_patient.ui", self)

        self.back_button.clicked.connect(self.close)
        self.save_button.clicked.connect(self.save_button_clicked)

        self.person_fields = get_widget_mapping(Person())
        for field_name, widget in self.person_fields.items():
            callback = self.make_editing_finished_callback(
                field_name, self.patient.person, widget
            )
            widget.editingFinished.connect(callback)
            self.field_list.addRow(field_name, widget)

    def save_button_clicked(self):
        # using the data in field_list, create a person object
        # and update the patient object
        print(json.dumps(self.patient.person.dict(), indent=4))
        try:
            self.patient.update_patient_info()
            self.close()
        except ValidationError as e:
            QMessageBox.about(self, "Validation Error", str(e))

    ...

    def make_editing_finished_callback(
        self, field_name: str, model: Person, widget: QtWidgets.QWidget
    ):
        def callback():
            # read the text from the widget
            value = widget.text()

            # validate the value
            try:
                setattr(model, field_name, value)
                # this might raise a # ValidationError
            except ValidationError as e:
                # display an error message and undo the change in the widget
                QMessageBox.about(self, "Validation Error", str(e))
                # assuming that the widget's text was set to the valid
                # model's field value
                # before connecting this callback. If that's not
                # the case, you'll have to
                # store the last valid value somewhere and restore it here
                widget.setText(getattr(model, field_name))

        return callback


def run():
    app = QtWidgets.QApplication([])
    win = NewPatient()
    win.show()
    app.exec_()


if __name__ == "__main__":
    run()
