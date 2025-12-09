import re
from itertools import product
from pathlib import Path
from typing import Optional, NamedTuple



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

    @property
    def max_area(self, strategy: str = "brute_force") -> int:
        """ Brute force """
        if strategy != "brute_force":
            raise NotImplementedError(f"Strategy {strategy} was not implemented yet")
        return self._brute_force_max_area()

    def _brute_force_max_area(self) -> int:
        max_area = 0
        for i, j in product(range(len(self.red_tiles)), range(1, len(self.red_tiles))):
            base = (
                max(self.red_tiles[i].x, self.red_tiles[j].x) -
                min(self.red_tiles[i].x, self.red_tiles[j].x)
            ) + 1
            height = (
                    max(self.red_tiles[i].y, self.red_tiles[j].y) -
                    min(self.red_tiles[i].y, self.red_tiles[j].y)
            ) + 1
            if base * height > max_area:
                max_area = base * height
        return max_area


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        floor = TileFloor(self.lines)
        return floor.max_area


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()