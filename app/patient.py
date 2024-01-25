import uuid
import json
from app.main import settings
from app.safe_write import safe_file_write


# create and manage a new patient record

def create_patient_id():
    """
    Create a new patient ID
    """
    return uuid.uuid4()


class Person:
    demographics = {
        "name": "Name",
        "address": "Address",
        "dob": "Date of Birth",
        "email": "Email",
        "phone": "Phone",
        "insurance": "Insurance"
    }

    def __init__(self, name: str, address: str,
                 dob: str, email: str, phone: str,
                 insurance: str):
        self.demographics["name"] = name
        self.demographics["address"] = address
        self.demographics["dob"] = dob
        self.demographics["email"] = email
        self.demographics["phone"] = phone
        self.demographics["insurance"] = insurance

    # Function to convert object to json returns a string.

    def to_json(self) -> str:
        return json.dumps(self.demographics)

    def get_info(self):
        return {k: (v, type(v).__name__)
                for k, v in self.demographics.items()}

    # Function to save data from a Qt widget callback
    def save_data(self, data):
        for k, v in data.items():
            self.demographics[k] = v


class Patient:
    """
    Class to create and manage a new patient record
    """

    def __init__(self, person_data_filename=None):
        # when no filename supplied, create a new person
        if not person_data_filename:
            self.patient_id = create_patient_id()
            self.person = Person(None, None, None,
                                 None, None, None)
        else:
            # try to load the person data from the file
            try:
                with open(person_data_filename, 'r') as file:
                    data = json.load(file)
                    # instantiate the Person class with the
                    # data from the file
                    self.patient_id = data.get('patient_id')
                    self.person = Person(
                        data.get('name'),
                        data.get('address'),
                        data.get('dob'),
                        data.get('email'),
                        data.get('phone'),
                        data.get('insurance')
                    )
            except Exception as e:
                raise ValueError('Unable to load data from the file. '
                                 'Error: {}'.format(e))

    def patient_json_export(self):
        """
        Export patient data as json
        """
        data_dir = settings.DATA_DIR
        file_name = self.patient_id
        file_path = data_dir + "/" + file_name
        print(file_path)
        try:
            safe_file_write(file_path, self.person.to_json())
        except IOError:
            print("Error: File does not appear to exist.")
        except Exception as e:
            print("Error: %s : %s" % ("data", e.strerror))

    def request_patient_info(self):
        """
        Method to request patient information
        should return a dictionary of patient information if
        there is data
        in the dict and a dict of types if there is no data
        """
        # TODO: Implement method to request patient information

    def update_patient_info(self):
        """
        Method to update patient information based on a callback
        from a Qt widget
        """
        # TODO: Implement method to return patient information
