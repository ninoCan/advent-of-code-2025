""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from advent_of_code_2025_python.day10.main import Machine
from src.advent_of_code_2025_python.day10.main import Solution


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(15, 18)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture
def machine_props():
    return (
        (
            ".##.",
            [[3], [1,3], [2], [2,3], [0,2], [0,1]],
            [3,5,4,7],
        ),
        (
            "...#.",
            [[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]],
            [7,5,12,7,2],
        ),
        (
            ".###.#",
            [[0,1,2,3,4], [0,3,4], [0,1,2,4,5], [1,2]],
            [10,11,11,5,10,5],
        ),
    )

def test_parse(provide_test_lines, machine_props):
    under_test = Solution.parse
    for i, line in enumerate(provide_test_lines):
        expected = machine_props[i]
        actual = under_test(line)
        assert actual == expected


@pytest.mark.parametrize(
    "machine,expected",
    (
        (0, 2),
        (1, 3),
        (2, 2),
    ),
    ids=["first_machine", "second_machine", "third_machine"]
)
def test_machines(machine_props, machine, expected):
    under_test = Machine(*machine_props[machine])
    actual = len(under_test.minimal_buttons_to_turn_on())
    assert actual == expected


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 7
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 33
    actual = under_test.second_task()
    assert actual == 33