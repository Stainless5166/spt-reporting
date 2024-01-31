import uuid
import json
from pydantic import BaseModel
from typing import Optional
from spt_reporting import SETTINGS
from app.safe_write import safe_file_write
import logging

logger = logging.getLogger(__name__)


# create and manage a new patient record


def create_patient_id():
    """
    Create a new patient ID
    """
    return uuid.uuid4()


class Person(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    insurance: Optional[str] = None


class Patient:
    """
    Class to create and manage a new patient record
    """

    def __init__(self, person_data_filename=None):
        # when no filename supplied, create a new person
        if not person_data_filename:
            self.patient_id = create_patient_id()
            self.person = Person()
        else:
            # try to load the person data from the file
            try:
                with open(person_data_filename, "r") as file:
                    data = json.load(file)
                    # instantiate the Person class with the
                    # data from the file
                    self.patient_id = data.get("patient_id")
                    self.person = Person(
                        name=data.name,
                        address=data.address,
                        dob=data.dob,
                        email=data.email,
                        phone=data.phone,
                        insurance=data.insurance,
                    )
            except Exception as e:
                raise ValueError(
                    "Unable to load data from the file. " "Error: {}".format(e)
                )

    def patient_json_export(self):
        """
        Export patient data as json
        """
        data_dir = SETTINGS.DATA_DIR
        file_name = self.patient_id
        file_path = data_dir + "/" + file_name
        logger.debug(file_path)
        try:
            safe_file_write(file_path, self.person.json())
        except IOError:
            logger.debug("Error: File does not appear to exist.")
        except Exception as e:
            logger.debug("Error: %s : %s" % ("data", e.strerror))

    def request_patient_info(self):
        """
        Method to request patient information
        should return a dictionary of patient information if
        there is data
        in the dict and a dict of types if there is no data
        """
        # TODO: Implement method to request patient information

    def update_patient_info(self, person: Person = None, test=None):
        """
        Method to update patient information based on a callback
        from a Qt widget
        """
        # update the self.person object with the data from the
        # person object passed to the method
        self.person = person
        # TODO: Implement method to return patient information
