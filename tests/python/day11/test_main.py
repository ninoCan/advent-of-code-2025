""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.advent_of_code_2025_python.day11.main import Solution, Device


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(21, 31)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture
def provide_test_lines_2() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(67, 80)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.mark.parametrize(
    "iteration,label,outputs",
    (
        (0, "aaa", ["you", "hhh"],),
        (1, "you", ["bbb", "ccc"],),
        (2, "bbb", ["ddd", "eee"],),
        (3, "ccc", ["ddd", "eee", "fff"],),
        (4, "ddd", ["ggg"],),
        (5, "eee", ["out"],),
        (6, "fff", ["out"],),
        (7, "ggg", ["out"],),
        (8, "hhh", ["ccc", "fff", "iii"],),
        (9, "iii", ["out"],),
    ),
)
def test_should_parse_Device_from_str(provide_test_lines, iteration, label, outputs) -> None:
    under_test = Device.from_str
    expected = Device(label, outputs)
    line_stub = provide_test_lines[iteration]
    actual = under_test(line_stub)
    assert actual == expected


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 5
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines_2: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines_2)
    expected = 2
    actual = under_test.second_task()
    assert actual == expected