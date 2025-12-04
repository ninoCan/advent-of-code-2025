from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Optional

from utils.python import Point
from utils.python.grid import Grid

@dataclass
class PrintingDepartment:
    grid: Grid
    removed_rolls: int = 0

    def count_neighbors_like(self, point: Point, char_to_match: str) -> int:
        neighboring_coords = [
            (point.x + x, point.y + y)
            for x in (-1, 0, 1)
            for y in (-1, 0, 1)
            if self.grid.width > point.x + x >= 0
               and self.grid.height > point.y + y >= 0
               and (x, y) != (0, 0)
        ]
        return sum(
            1
            for coord_pair in neighboring_coords
            if self.grid.data[coord_pair[0], coord_pair[1]] == char_to_match
        )

    @property
    def suitable_spots(self) -> int:
        return sum(
            1
            for x, y in product(range(self.grid.width), range(self.grid.height))
            if self.grid.data[x, y] == "@"
            and self.count_neighbors_like(Point(x, y), "@") < 4
        )

    def remove_roll(self, point: Point) -> None:
        self.grid.data[point.x, point.y] = "."
        self.removed_rolls += 1


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with (open(path) as file):
            raw_lines =file.readlines() if not lines else lines
            self.lines = [
                line.strip() for line in raw_lines
            ]

    def first_task(self) -> int:
        dep = PrintingDepartment(Grid(self.lines))
        return dep.suitable_spots


    def second_task(self) -> int:
        dep = PrintingDepartment(Grid(self.lines))
        while dep.suitable_spots > 0:
            for x, y in product(range(dep.grid.width), range(dep.grid.height)):
                if dep.grid.data[x, y] == ".":
                    continue
                if dep.count_neighbors_like(Point(x, y), "@") < 4:
                    dep.remove_roll(Point(x, y))
        return dep.removed_rolls

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()