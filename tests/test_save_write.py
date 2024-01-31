import os
import pytest
from app.safe_write import safe_file_write


def test_file_creation():
    """Test if the file and folder are created if they don't exist."""
    path = "temp/test_file.txt"
    data = "test data"
    safe_file_write(path, data)
    assert os.path.exists(path)
    with open(path, "r") as file:
        assert file.read() == data
    os.remove(path)
    os.rmdir("temp")


def test_existing_file():
    """Test writing to an existing file."""
    path = "temp/test_file.txt"
    os.makedirs("temp", exist_ok=True)
    with open(path, "w") as file:
        file.write("initial data")
    new_data = "new test data"
    safe_file_write(path, new_data)
    with open(path, "r") as file:
        assert file.read() == new_data
    os.remove(path)
    os.rmdir("temp")


def test_ioerror_handling():
    """Test IOError handling (e.g., no write permission)."""
    path = "/test_file.txt"
    data = "test data"
    with pytest.raises(Exception):
        safe_file_write(path, data)


# Mocking unexpected errors is a bit more complex
# and might involve patching
# or using a testing framework that allows injecting faults.
