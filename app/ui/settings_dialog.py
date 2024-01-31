import sys
import json
from PyQt5 import QtWidgets, uic


class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        uic.loadUi("settings_dialog.ui", self)

        self.settings_widgets = {}
        self.settings_file_path = "settings.json"

        self.load_from_file()

        # Connect saveButton's clicked signal to our save method
        self.saveButton.clicked.connect(self.save_settings)

    def load_from_file(self):
        # Frozen or not
        if getattr(sys, "frozen", False):
            current_path = sys._MEIPASS
        else:
            current_path = ""

        with open(
            current_path + self.settings_file_path, "r"
        ) as settings_file:
            settings = json.load(settings_file)

            # Iterate over all loaded settings
            for key, value in settings.items():
                # Create a QLabel and QLineEdit for each setting
                label = QtWidgets.QLabel(f"{key}:")
                line_edit = QtWidgets.QLineEdit()

                # Set the current value in QLineEdit
                line_edit.setText(str(value))

                # Add them to the scroll area's formLayoutWidget layout
                self.formLayoutWidget.layout().addRow(label, line_edit)

                # Store the QLineEdit in our dictionary
                self.settings_widgets[key] = line_edit

    def save_settings(self):
        # Save settings from each QLineEdit to a json file
        settings_to_save = {}
        for key, line_edit in self.settings_widgets.items():
            value = line_edit.text()
            settings_to_save[key] = value

        with open(self.settings_file_path, "w") as settings_file:
            json.dump(settings_to_save, settings_file)
