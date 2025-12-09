import re
from itertools import product
from pathlib import Path
from typing import Optional, NamedTuple
from shapely.geometry import LineString, Polygon


class RedTile(NamedTuple):
    x: int
    y: int


class TileFloor:
    PATTERN = re.compile(r'(\d+)')

    def __init__(self, lines: list[str]):
        self.red_tiles = [
            RedTile(*[
                int(el)
                for el in re.findall(self.PATTERN, line)
            ]) for line in lines
        ]
        self.green_polygon = Polygon(self.red_tiles)

    def rectangle_area(self, i: int, j: int) -> int:
        base = (
                       max(self.red_tiles[i].x, self.red_tiles[j].x) -
                       min(self.red_tiles[i].x, self.red_tiles[j].x)
               ) + 1
        height = (
                         max(self.red_tiles[i].y, self.red_tiles[j].y) -
                         min(self.red_tiles[i].y, self.red_tiles[j].y)
                 ) + 1
        return base * height

    def max_area(self, strategy: str = "brute_force") -> int:
        if strategy == "diagonals_within":
            return self._diagonals_within_max_area()
        if strategy != "brute_force":
            raise NotImplementedError(f"Strategy {strategy} was not implemented yet")
        return self._brute_force_max_area()

    def _brute_force_max_area(self) -> int:
        max_area = 0
        for i, j in product(range(len(self.red_tiles)), range(1, len(self.red_tiles))):
            if (area:=self.rectangle_area(i, j)) > max_area:
                max_area = area
        return max_area


    def _diagonals_within_max_area(self):
        max_area = 0
        for i, j in product(range(len(self.red_tiles)), range(1, len(self.red_tiles))):
            diagonal = LineString([self.red_tiles[i], self.red_tiles[j]])
            antidiag = LineString([
                (self.red_tiles[i].x, self.red_tiles[j].y),
                (self.red_tiles[j].x, self.red_tiles[i].y)
            ])
            if (
                self.green_polygon.contains(diagonal)
                and self.green_polygon.contains(antidiag)
                and (area := self.rectangle_area(i, j)) > max_area
            ):
                max_area = area
        return max_area


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        floor = TileFloor(self.lines)
        return floor.max_area()


    def second_task(self) -> int:
        floor = TileFloor(self.lines)
        return floor.max_area(strategy="diagonals_within")


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()