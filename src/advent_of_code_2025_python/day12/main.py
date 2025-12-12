import re
from dataclasses import dataclass
from functools import cached_property, cache
from itertools import product, chain, batched
from pathlib import Path
from pyexpat.errors import XML_ERROR_ASYNC_ENTITY
from typing import Optional

from shapely import box
from shapely.geometry.base import BaseGeometry
from shapely.ops import unary_union

from utils.python import Point, flatten

AMOUNT_PATTERN = re.compile(r"\d+")

@dataclass(frozen=True)
class Gift:
    id_number: int
    empty_spots: list[Point]

    @property
    def polygon(self) -> BaseGeometry:
        filled_cells = [
            box(x, y, x + 1, y + 1)
            for x, y in product(range(3), repeat=2)
            if (x, y) not in self.empty_spots
        ]
        return unary_union(filled_cells)

    @property
    def area(self) -> int:
        return 9 - len(self.empty_spots)

    @staticmethod
    def from_lines(lines: list[str]) -> Gift:
        first, *rest = lines
        id_number =  int(first[0])
        empty_spots = [
            Point(x, y)
            for y, line in enumerate(rest)
            for x, char in enumerate(line)
            if char == "."
        ]
        return Gift(id_number, empty_spots)


class XmasTree:
    def __init__(self, line: str, gift_catalog: dict[int, Gift]):
        [dimensions, gifts] = line.split(":")
        [width, height] = dimensions.split("x")
        self.width = int(width)
        self.height = int(height)
        self.gift_amounts = list(re.findall(AMOUNT_PATTERN, gifts))
        self.gifts = self.make_gifts(gift_catalog)

    def make_gifts(self, catalog: dict[int, Gift]) -> list[Gift]:
        return list(chain.from_iterable(
            [catalog[id_number]] * int(amount)
            for id_number, amount in enumerate(self.gift_amounts)
        ))


    @property
    def can_fit_gifs(self) -> bool:
        if sum(gift.area for gift in self.gifts) > self.width * self.height:
            return False
        # if self.minimal_pack(self.gifts) > (self.width, self.height):
        #     return False
        return True


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            raw_lines = file.readlines() if not lines else lines
            self.lines = [
                line.strip("\n")
                for line in raw_lines
            ]

    def first_task(self) -> int:
        shape_lines, tree_lines = self.lines[:30], self.lines[30:]
        catalog = {
            id_: Gift.from_lines(lines[:-1])
            for id_, lines in enumerate(batched(shape_lines, 5))
        }
        trees = [XmasTree(line, catalog) for line in tree_lines]
        return sum(
            1
            for tree in trees
            if tree.can_fit_gifs
        )

    def second_task(self) -> int:
        return "completing previous stars."

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()