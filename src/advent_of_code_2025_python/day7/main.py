from pathlib import Path
from typing import Optional


class TachionManifold:
    SOURCE = "S"
    BEAM = "|"
    SPLITTER = "^"
    PAIR = "|^|"

    def __init__(self, lines: list[str]):
        self.field = lines
        self.beams_split = 0
        self.beam_area = 0

    def evolve(self) -> int:
        if self.BEAM in self.field[1]:
            return self.beams_split
        beams_positions = self.fire_tachyonic_beam()
        for index in range(1, len(self.field)):
            if index % 2 == 0:
                self.split_beams(beams_positions, index)
            else:
                self.propagate_beams(beams_positions, index)
        return self.beams_split


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        pass


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()