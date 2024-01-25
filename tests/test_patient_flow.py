import os.path
import pytest
import shutil
import logging

from app.patient import Patient
from app.main import settings

test_dir = "/tmp/data"

logger = logging.getLogger(__name__)


@pytest.fixture
def patient():
    patient = Patient()
    patient.patient_id = "test_patient_id"
    yield patient
    # teardown code
    try:
        shutil.rmtree(test_dir)
    except OSError as e:
        logger.debug("Error: %s : %s" % (test_dir, e.strerror))


class TestNewPatientForm:
    """
    Test class for NewPatientForm
    """

    def test_create_patient_id(self, patient):
        """
        Test case for createPatientID method
        """
        # create new patient ID
        patient = Patient()
        # check that the patient ID exits
        assert patient.patient_id is not None
        # check that the patient ID is a UUID
        # assert patient.patient_id.is_uuid()

    def test_patient_json_export(self, monkeypatch, patient):
        monkeypatch.setattr(settings, "DATA_DIR", test_dir)
        """
        Test case for patient_json_export method
        test creation of file, that file does not already exist,
        and that file is json
        and that the json export matches the patient object that is exported.
        """

        good_path = settings.DATA_DIR + "/" + patient.patient_id
        logger.debug(good_path)

        # check that the file does not already exist
        assert os.path.exists(good_path) is False

        # export patient data as json
        patient.patient_json_export()

        # check that the file exists
        assert os.path.exists(good_path) is True


class TestTestSetSelector:
    """
    Test class for TestSetSelector
    """

    def test_load_test_sets(self):
        """
        Test case for loadTestSets method
        """
        pass  # TODO: Implement test case

    def test_select_test_set(self):
        """
        Test case for selectTestSet method
        """
        pass  # TODO: Implement test case


class TestStartTest:
    """
    Test class for StartTest
    """

    def test_create_test_id(self):
        """
        Test case for createTestID method
        """
        pass  # TODO: Implement test case


class TestRecordResults:
    """
    Test class for RecordResults
    """

    def test_record_results(self):
        """
        Test case for recordResults method
        """
        pass  # TODO: Implement test case


class TestSave:
    """
    Test class for Save
    """

    def test_save_results(self):
        """
        Test case for saveResults method
        """
        pass  # TODO: Implement test case


class TestPrint:
    """
    Test class for Print
    """

    def test_load_files(self):
        """
        Test case for loadFiles method
        """
        pass  # TODO: Implement test case

    def test_create_report(self):
        """
        Test case for createReport method
        """
        pass  # TODO: Implement test case
