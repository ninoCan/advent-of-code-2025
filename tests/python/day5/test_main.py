""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.advent_of_code_2025_python.day5.main import Solution



@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(23, 34)
        return [line.strip() for line in file.readlines()[example_slice]]



def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 3
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=[
        "3-5\n",
        "10-14\n",
        "14-14\n",
        "16-20\n",
        "12-18\n",
        "3-3\n",
        "21-21\n",
        "\n",
        "241\n",
    ])
    expected = 15
    actual = under_test.second_task()
    assert actual == expected