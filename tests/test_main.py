import pytest
from app.ui.main_controller import YourMainWindowClass


@pytest.fixture
def main_window(qtbot):
    window = YourMainWindowClass()
    qtbot.addWidget(window)
    return window


def test_open_close_window(main_window, qtbot):
    main_window.show()
    with qtbot.waitExposed(main_window):
        qtbot.waitUntil(main_window.isVisible)
    main_window.close()
    assert not main_window.isVisible()


def test_start_stop_program(main_window):
    assert main_window.start_program()
    assert main_window.stop_program()


# Load a configuration file if available
def test_load_config_file_if_available():
    pass
