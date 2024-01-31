import pytest
import logging
from PyQt5.QtWidgets import QApplication
from unittest.mock import patch
from app.ui.new_patient import NewPatient


@pytest.fixture(scope="session", autouse=True)
def app_context():
    logger = logging.getLogger()
    logger.info("Starting application context")
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def new_patient():
    """
    Create a new patient instance for testing purposes.

    :return: Instance of NewPatient class
    """
    # create an instance for the test
    new_patient = NewPatient()
    return new_patient


def test_new_patient_save_button(new_patient):
    # assert if the save button is enabled
    assert new_patient.save_button.isEnabled()
    logging.debug("Save button is enabled")


def test_new_patient_back_button(new_patient):
    # assert if the back button is enabled
    assert new_patient.back_button.isEnabled()


@patch("app.ui.new_patient.QMessageBox")
def test_is_valid_without_error(mock_msg_box, new_patient):
    # trigger the method
    new_patient.save_button_clicked()
    # check if QMessageBox.about was called indicating no validation error
    mock_msg_box.about.assert_not_called()
