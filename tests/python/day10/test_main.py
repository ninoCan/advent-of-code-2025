""" This is a template file do not use it directly.
"""
from dataclasses import dataclass
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.advent_of_code_2025_python.day10.main import Solution

@dataclass(frozen=True)
class Machine:
    light_diagram: str
    buttons: list[list[int]]
    joltage_reqs: list[int]

    @property
    def minimal_buttons_to_turn_on(self) -> tuple[int, list[int]]:
        pass

@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(15, 18)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_first_machine():
    under_test = Machine(
        ".##.",
        [[3], [1,3], [2], [2,3], [0,2], [0,1]],
        [3,5,4,7]
    )
    expected = 2
    actual = under_test.minimal_buttons_to_turn_on[0]
    assert actual == expected


def test_second_machine():
    under_test = Machine(
        "...#.",
        [[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]],
        [7,5,12,7,2]
    )
    expected = 3
    actual = under_test.minimal_buttons_to_turn_on[0]
    assert actual == expected


def test_third_machine():
    under_test = Machine(
        ".###.#",
        [[0,1,2,3,4], [0,3,4], [0,1,2,4,5], [1,2]],
        [10,11,11,5,10,5],
    )
    expected = 2
    actual = under_test.minimal_buttons_to_turn_on[0]
    assert actual == expected


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 7
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = "placeholder"
    actual = under_test.second_task()
    assert actual == expected