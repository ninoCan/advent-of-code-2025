""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from advent_of_code_2025_python.day2.main import Solution, IDSpan
from utils.python.html_code_parser import CodeExtractor


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(61, 72)
        return [line.strip() for line in file.readlines()[example_slice]]

@pytest.fixture
def provide_test_line() -> str:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(22, 25)
        return "".join([line.strip() for line in file.readlines()[example_slice]])



def test_first_task(provide_test_line: list[str]) -> None:
    under_test = Solution(lines=provide_test_line)
    expected = 1227775554
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_line: list[str]) -> None:
    under_test = Solution(lines=provide_test_line)
    expected = 4174379265
    actual = under_test.second_task()
    assert actual == expected


def test_sieve_ids_with_repeating_digits(provide_test_lines):
    under_test = IDSpan
    for line in provide_test_lines:
        parser = CodeExtractor()
        parser.feed(line)
        input_stub, *expected = parser.results
        actual = under_test(input_stub).sieve_ids_with_repeating_digits()
        assert actual == [int(el) for el in expected], f"Fails on {input_stub}"

