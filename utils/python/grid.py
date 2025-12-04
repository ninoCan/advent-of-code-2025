from itertools import product
from typing import Sequence, Iterator

import numpy as np

from utils.python.point import Point
from utils.python.directions import Direction


class Grid:
    def __init__(self, data: Sequence[str]):
        self.width = len(data[0].strip("\n"))
        self.height = len(data)
        self.data = (
            np.char.asarray([[letter for letter in row] for row in data])
            if data
            else np.char.asarray([])
        )

    def locate(self, char: str):
        return np.argwhere(self.data == char)

    def is_inside(self, point: Point) -> bool:
        if 0 <= point.x < self.width and 0 <= point.y < self.height:
            return True
        return False

    @staticmethod
    def next_position(current: Point, direction: Direction) -> Point:
        match direction.value:
            case "^":
                return Point(current.x, current.y + 1)
            case ">":
                return Point(current.x + 1, current.y)
            case "v":
                return Point(current.x, current.y - 1)
            case "<":
                return Point(current.x - 1, current.y)

    @property
    def rows(self) -> list[str]:
        return ["".join(row) for row in self.data]

    @property
    def columns(self) -> list[str]:
        return ["".join(col) for col in self.data.T]

    @property
    def main_diagonals(self) -> list[str]:
        return [
            "".join(self.data.diagonal(offset))
            for offset in range(-self.width + 1, self.width)
        ]

    @property
    def anti_diagonals(self) -> list[str]:
        return [
            "".join(np.fliplr(self.data).diagonal(offset))
            for offset in range(-self.width + 1, self.width)
        ]

    @property
    def diagonals(self) -> list[str]:
        return self.main_diagonals + self.anti_diagonals

    def copy(self) -> "Grid":
        return Grid(self.data.copy())

    def points(self) -> Iterator[Point]:
        for x, y in product(range(self.width), range(self.height)):
            yield Point(x, y)

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
            if self.data[coord_pair[0], coord_pair[1]] == char_to_match
        )
