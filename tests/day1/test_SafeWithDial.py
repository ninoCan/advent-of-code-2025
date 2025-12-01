from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day1.main import SafeWithDial

@pytest.fixture()
def provide_safe():
    return SafeWithDial(pointing_at=50)

def test_should_rotate_left(provide_safe):
    safe = provide_safe

    for degrees in range(100):
        expected = (50 - degrees) % 100
        actual = safe.rotate_left(degrees)
        assert actual.dial_number == expected
        safe = SafeWithDial()

def test_should_rotate_right(provide_safe):
    safe = provide_safe

    for degrees in range(100):
        expected = (50 + degrees) % 100
        actual = safe.rotate_right(degrees)
        assert actual.dial_number == expected
        safe = SafeWithDial()
