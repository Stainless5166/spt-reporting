import json

# import pytest
from app.patient import Person


def test_person_initialization():
    name = "John Doe"
    address = "123 Elm St"
    dob = "1990-01-01"
    email = "johndoe@email.com"
    phone = "123-456-7890"
    insurance = "XYZ123"

    person = Person(
        name=name,
        address=address,
        dob=dob,
        email=email,
        phone=phone,
        insurance=insurance,
    )

    assert person.name == name
    assert person.address == address
    assert person.dob == dob
    assert person.email == email
    assert person.phone == phone
    assert person.insurance == insurance


def test_person_to_dict():
    name = "John Doe"
    address = "123 Elm St"
    dob = "1990-01-01"
    email = "johndoe@email.com"
    phone = "123-456-7890"
    insurance = "XYZ123"

    person = Person(
        name=name,
        address=address,
        dob=dob,
        email=email,
        phone=phone,
        insurance=insurance,
    )
    # use person.json() to convert to json
    person_dict = person.json()

    assert person_dict == json.dumps(
        {
            "name": name,
            "address": address,
            "dob": dob,
            "email": email,
            "phone": phone,
            "insurance": insurance,
        }
    )


def test_person_save_data():
    name = "John Doe"
    address = "123 Elm St"
    dob = "1990-01-01"
    email = "johndoe@email.com"
    phone = "123-456-7890"
    insurance = "XYZ123"

    person = Person(
        name=name,
        address=address,
        dob=dob,
        email=email,
        phone=phone,
        insurance=insurance,
    )

    new_data = {
        "name": "Jane Doe",
        "address": "456 Pine St",
        "dob": "1992-02-02",
        "email": "janedoe@email.com",
        "phone": "098-765-4321",
        "insurance": "ABC987",
    }

    person = Person(**new_data)

    assert person.name == new_data["name"]
    assert person.address == new_data["address"]
    assert person.dob == new_data["dob"]
    assert person.email == new_data["email"]
    assert person.phone == new_data["phone"]
    assert person.insurance == new_data["insurance"]
