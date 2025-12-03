""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.advent_of_code_2025_python.day3.main import Solution, BatteryBank


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(25, 29)
        return [line.strip() for line in file.readlines()[example_slice]]



def test_first_task(provide_test_lines) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 357
    actual = under_test.first_task()
    assert actual == expected


def test_max_joltage(provide_test_lines):
    expectations = [98, 89, 78, 92]
    under_test = BatteryBank
    for ind, line in enumerate(provide_test_lines):
        actual = under_test(line).max_joltage
        assert actual == expectations[ind], f"Fails on line {ind}: {line}"


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 3121910778619
    actual = under_test.second_task()
    assert actual == expected