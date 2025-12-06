import re
from copy import deepcopy
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from string import digits
from typing import Optional



class Operator(StrEnum):
    PLUS = "+"
    PROD = "*"

ops = {
    "+": Operator.PLUS,
    "*": Operator.PROD,
}

class Worksheet:
    @dataclass
    class Column:
        operands: str
        operator_to_use: Operator

        @property
        def total(self):
            return eval(self.operator_to_use.join(self.operands))

    def __init__(self, lines: list[str]):
        columns = self.parse_columns(deepcopy(lines))
        self.columns = [
            self.Column(col[:-1], ops[col[-1]])
            for col in columns
            if col[-1] in ("+", "*")
        ]

    @property
    def sum_totals(self):
        return sum(col.total for col in self.columns)

    def parse_columns(self, lines: list[str]):
        pattern = r"\d+"
        re.compile(pattern)
        operations_to_perform = [
            el
            for el in lines.pop(len(lines) - 1).split(" ")
            if el != ""
        ][:-1]
        digits = [
            re.findall(pattern, line)
            for line in lines
        ]
        return [
            [el[ind] for el in digits] + [op]
            for ind, op in enumerate(operations_to_perform)
        ]



class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            raw_lines = file.readlines() if not lines else lines
            self.lines = [line for line in raw_lines if line != "\n"]

    def first_task(self) -> int:
        wkst = Worksheet(self.lines)
        return sum(col.total for col in wkst.columns)

    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()