import logging
import sys

from pathlib import Path
from typing import Optional, Self

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class SafeWithDial:
    def __init__(
            self,
            pointing_at: int = 50,
            visited_zero: Optional[int] = None,
    ):
        self.dial_number = pointing_at
        self.visited_zero = visited_zero if visited_zero else 0

    def __str__(self):
        return f"SafeWithDial({self.dial_number=}, {self.visited_zero=})"

    def rotate_left(self, degrees: int) -> Self:
        """
        Rotate anti-clockwise reducing the dial number by the amount of degrees provided.

        Args
          degrees: integer number of degrees
        """
        new_safe = SafeWithDial(
            pointing_at=((self.dial_number - degrees) % 100),
            visited_zero=self.visited_zero,
        )
        if new_safe.dial_number == 0:
            return SafeWithDial(new_safe.dial_number, new_safe.visited_zero + 1)
        return new_safe

    def rotate_right(self, degrees: int) -> Self:
        """
        Rotate clockwise increasing the dial number by the amount of degrees provided.

        Args
          degrees: integer number of degrees
        """
        new_safe = SafeWithDial(
            pointing_at=((self.dial_number + degrees) % 100),
            visited_zero=self.visited_zero,
        )
        if new_safe.dial_number == 0:
            return SafeWithDial(new_safe.dial_number, new_safe.visited_zero + 1)
        return new_safe



    def batch(self, instructions: list[str]) -> Self:
        if not instructions:
            return self
        direction, degree = instructions[0][0], int(instructions[0][1:])
        if direction == "L":
            return SafeWithDial(self.dial_number, self.visited_zero).rotate_left(degree).batch(instructions[1:])
        elif direction == "R":
            return SafeWithDial(self.dial_number, self.visited_zero).rotate_right(degree).batch(instructions[1:])
        raise ValueError("Invalid direction")



class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            raw_lines = file.readlines() if not lines else lines
            self.lines = [
                line.strip("\n")
                for line in raw_lines
                if len(line) > 0
            ]

    def first_task(self) -> int:
        new_recursion_limit = len(self.lines) + 10
        if new_recursion_limit > sys.getrecursionlimit():
            sys.setrecursionlimit(new_recursion_limit)
        safe = SafeWithDial()
        final_safe = safe.batch(self.lines)
        return final_safe.visited_zero


    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
