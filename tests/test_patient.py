import os
import pytest
from pathlib import Path
from app.patient import Patient
from dynaconf import settings

# Your module and actual values can be different. Please replace accordingly.


@pytest.fixture
def setup_patient():
    p1 = Patient()
    p1.patient_id = "patient_id"
    p1.json_export()  # Be sure to use the correct method name here
    yield p1

    # Deleting the file after test
    file_name = str(p1.patient_id) + ".json"
    file_path = Path(settings.DATA_DIR, file_name)
    if file_path.exists():
        os.remove(file_path)


def test_patient_creation():
    p = Patient()
    assert isinstance(p, Patient), "Object is not an instance of Patient class"


def test_patient_save():
    # Create new Patient and save information.
    p = Patient()
    assert isinstance(p, Patient), "Object is not an instance of Patient class"
    default_file_path = Path(settings.DATA_DIR, str(p.patient_id) + ".json")
    p.json_export()

    # Check if the patient info was saved correctly.
    assert default_file_path.exists(), f"File {default_file_path} does not exist"


def test_patient_load(setup_patient):
    p2 = Patient("patient_id.json")
    assert isinstance(p2, Patient), "Object is not an instance of Patient class"
