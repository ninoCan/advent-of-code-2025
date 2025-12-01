import logging

from pathlib import Path
from typing import Optional, Self
from venv import logger

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class SafeWithDial:
    def __init__(self, pointing_at: int = 50):
        self.dial_number = pointing_at

    def rotate_left(self, degrees: int) -> Self:
        """
        Rotate anti-clockwise reducing the dial number by the amount of degrees provided.

        Args
          degrees: integer number of degrees
        """
        logging.info(f"Rotating dial {self.dial_number} of degrees {degrees} to the left")
        logger.debug(f"Expecting {(self.dial_number - degrees) % 100}")
        new_safe = SafeWithDial(pointing_at=((self.dial_number - degrees) % 100))
        logger.debug(new_safe.dial_number)
        return new_safe

    def rotate_right(self, degrees: int) -> Self:
        """
        Rotate clockwise increasing the dial number by the amount of degrees provided.

        Args
          degrees: integer number of degrees
        """
        logging.info(f"Rotating dial {self.dial_number} of degrees {degrees} to the right")
        logger.debug(f"Expecting {(self.dial_number + degrees) % 100}")
        new_safe = SafeWithDial(pointing_at=((self.dial_number + degrees) % 100))
        logger.debug(new_safe.dial_number)
        return new_safe



    def batch(self, instructions: list[str]) -> int:
        if instructions[0] == "":
            return self.dial_number
        direction, degree = instructions[0][0], int(instructions[0][1:])
        if direction == "L":
            return SafeWithDial(self.dial_number).rotate_left(degree).batch(instructions[1:])
        elif direction == "R":
            return SafeWithDial(self.dial_number).rotate_right(degree).batch(instructions[1:])
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
        safe = SafeWithDial()
        return safe.batch(self.lines)

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
