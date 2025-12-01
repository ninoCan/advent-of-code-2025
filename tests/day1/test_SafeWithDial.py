from inspect import getsourcefile
from pathlib import Path
from .test_main import provide_test_lines

import pytest

from src.day1.main import SafeWithDial, SafeWithDialPassByZeroDetector

def test_should_rotate_left():
    safe = SafeWithDial()

    for degrees in range(100):
        expected = (50 - degrees) % 100
        actual = safe.rotate_left(degrees)
        assert actual.dial_number == expected
        safe = SafeWithDial()

def test_should_rotate_right():
    safe = SafeWithDial()

    for degrees in range(100):
        expected = (50 + degrees) % 100
        actual = safe.rotate_right(degrees)
        assert actual.dial_number == expected
        safe = SafeWithDial()

def test_should_execute_batch(provide_test_lines):
    safe = SafeWithDial()
    expected = 32
    actual = safe.batch(provide_test_lines)
    assert actual.dial_number == expected
    assert actual.visited_zero == 3

def test_should_execute_batch_with_pass_by_zero(provide_test_lines):
    safe = SafeWithDialPassByZeroDetector()
    expected = 32
    actual = safe.batch(provide_test_lines)
    assert actual.dial_number == expected
    assert actual.visited_zero == 6
