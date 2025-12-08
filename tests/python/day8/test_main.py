""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.advent_of_code_2025_python.day8.main import Solution, PlayGround


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(25, 45)
        return [line.strip() for line in file.readlines()[example_slice]]

def test_find_closest_pair_indices(provide_test_lines):
    under_test = PlayGround(provide_test_lines).find_n_closest_pair_indices
    expected = [(0, 19), (0, 7), (2, 13),(7, 19)]
    actual = under_test(4)
    assert [*actual] == expected


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 40
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 25272
    actual = under_test.second_task()
    assert actual == expected