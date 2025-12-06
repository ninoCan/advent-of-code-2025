import re
from copy import deepcopy
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
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
        operands: list[str]
        operator_to_use: Operator

        @property
        def total(self) -> int:
            return eval(self.operator_to_use.join(self.operands))

    def __init__(self, lines: list[str], cephalopod: bool=False):
        copied = deepcopy(lines)
        columns = self.parse_columns(copied) if not cephalopod else self.parse_ceph(copied)
        self.columns = [
            self.Column(col[:-1], ops[col[-1]])
            for col in columns
            if col and col[-1] in ("+", "*")
        ]

    @property
    def sum_totals(self) -> int:
        return sum(col.total for col in self.columns)

    def parse_columns(self, lines: list[str]) -> list[list[str]]:
        pattern = r"\d+"
        re.compile(pattern)
        operators = [
            item
            for item in lines.pop(len(lines) - 1).split(" ")
            if item != ""
        ][:-1]
        operands = [
            re.findall(pattern, line)
            for line in lines
        ]
        return [
            [el[ind] for el in operands] + [op]
            for ind, op in enumerate(operators)
        ]

    def parse_ceph(self, lines: list[str]) -> list[list[str]]:
        transposed = "|".join(["".join(chars) for chars in zip(*lines)])
        clusters = transposed.split("|" + " " * len(lines) + "|")
        op_pattern = r"[*+]"
        pattern = r"\d+"
        return [
            re.findall(pattern, cluster) + re.findall(op_pattern, cluster)
            for cluster in clusters
        ]


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            raw_lines = file.readlines() if not lines else lines
            self.lines = [line for line in raw_lines if line != "\n"]

    def first_task(self) -> int:
        wkst = Worksheet(self.lines)
        return wkst.sum_totals

    def second_task(self) -> int:
        wkst = Worksheet(self.lines, cephalopod=True)
        return wkst.sum_totals

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()