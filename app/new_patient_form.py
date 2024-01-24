import uuid
from app.main import settings
from app.safe_write import safe_file_write


# create and manage a new patient record

def create_patient_id():
    """
    Create a new patient ID
    """
    return uuid.uuid4()


class Patient:
    """
    Class to create and manage a new patient record
    """

    def __init__(self):
        self.patient_id = create_patient_id()

    def patient_json_export(self):
        """
        Export patient data as json
        """
        data_dir = settings.DATA_DIR
        file_name = self.patient_id
        file_path = data_dir + "/" + file_name
        print(file_path)
        try:
            safe_file_write(file_path, self.patient_id)
        except IOError:
            print("Error: File does not appear to exist.")
        except Exception as e:
            print("Error: %s : %s" % ("data", e.strerror))
