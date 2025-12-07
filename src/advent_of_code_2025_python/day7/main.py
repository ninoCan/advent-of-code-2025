import re
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
        """ Populate the field with the tachion beam and return the number of splits """
        if self.BEAM in self.field[1]:
            return self.beams_split
        beams_positions = self.fire_tachyonic_beam()
        for index in range(1, len(self.field)):
            if index % 2 == 0:
                self.split_beams(beams_positions, index)
            else:
                self.propagate_beams(beams_positions, index)
        return self.beams_split

    def fire_tachyonic_beam(self) -> set[int]:
        first_row = self.field[1]
        source_x = self.field[0].index(self.SOURCE)
        self.field[1] = first_row[:source_x] + self.BEAM + first_row[source_x + 1:]
        self.beam_area += 1
        return {source_x}

    def split_beams(self, positions: set[int], row_num: int) -> None:
        row =  self.field[row_num]
        splitters = re.finditer(r"[\^]", row)
        for x in (match.start() for match in splitters):
            if x in positions:
                self.field[row_num] = row[:x - 1] + self.PAIR + row[x + 2:]
                positions.remove(x)
                positions.add(x - 1)
                positions.add(x +1)
                self.beams_split += 1
                self.beam_area += 2

    def propagate_beams(self, positions: set[int], row_num: int) -> None:
        row =  self.field[row_num]
        for x in positions:
            self.field[row_num] = row[:x] + self.BEAM + row[x + 1:]
            self.beam_area += 1


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        manifold = TachionManifold(self.lines)
        return manifold.evolve()

    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()