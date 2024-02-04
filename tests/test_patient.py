from pathlib import Path
from app.patient import Patient
from dynaconf import settings

# Your module and actual values can be different. Please replace accordingly.


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


def test_patient_load():
    # Here we're assuming that 'test_patient_save' has already created a patient file.
    # Ideally, 'load' tests should not depend on 'save' tests.
    # Replace 'patient_id.json' with a valid test patient file.
    p1 = Patient()
    p1.patient_id = "patient_id"
    p1.json_export()
    p2 = Patient("patient_id.json")
    assert isinstance(p2, Patient), "Object is not an instance of Patient class"
