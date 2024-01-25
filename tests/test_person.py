import json

# import pytest
from app.patient import Person


def test_person_initialization():
    name = 'John Doe'
    address = '123 Elm St'
    dob = '1990-01-01'
    email = 'johndoe@email.com'
    phone = '123-456-7890'
    insurance = 'XYZ123'

    person = Person(name, address, dob, email, phone, insurance)

    assert person.demographics["name"] == name
    assert person.demographics["address"] == address
    assert person.demographics["dob"] == dob
    assert person.demographics["email"] == email
    assert person.demographics["phone"] == phone
    assert person.demographics["insurance"] == insurance


def test_person_to_dict():
    name = 'John Doe'
    address = '123 Elm St'
    dob = '1990-01-01'
    email = 'johndoe@email.com'
    phone = '123-456-7890'
    insurance = 'XYZ123'

    person = Person(name, address, dob, email, phone, insurance)
    # use person.json() to convert to json
    person_dict = person.to_json()

    assert person_dict == json.dumps({
        'name': name,
        'address': address,
        'dob': dob,
        'email': email,
        'phone': phone,
        'insurance': insurance
    })


def test_person_save_data():
    name = 'John Doe'
    address = '123 Elm St'
    dob = '1990-01-01'
    email = 'johndoe@email.com'
    phone = '123-456-7890'
    insurance = 'XYZ123'

    person = Person(name, address, dob, email, phone, insurance)
    new_data = {
        'name': 'Jane Doe',
        'address': '456 Pine St',
        'dob': '1992-02-02',
        'email': 'janedoe@email.com',
        'phone': '098-765-4321',
        'insurance': 'ABC987'
    }

    person.save_data(new_data)

    assert person.demographics['name'] == new_data['name']
    assert person.demographics['address'] == new_data['address']
    assert person.demographics['dob'] == new_data['dob']
    assert person.demographics['email'] == new_data['email']
    assert person.demographics['phone'] == new_data['phone']
    assert person.demographics['insurance'] == new_data['insurance']
