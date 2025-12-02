from functools import reduce
from itertools import chain
from pathlib import Path
from typing import Optional



class IDSpan:
    def __init__(self, id_range: str):
        self.start_at, self.end_at = id_range.split("-")

    @staticmethod
    def is_id_invalid(id_number: int) -> bool:
        code = str(id_number)
        if (size := len(str(code))) % 2 != 0:
            return False
        half = size // 2
        return code[:half] == code[half:]

    def sieve_invalid_ids(self) -> list[int]:
        return [
            item
            for item in range(int(self.start_at), int(self.end_at)+1)
            if self.is_id_invalid(item)
        ]

class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.line = file.readline() if not lines else lines

    def parse_input(self) -> list[str]:
        return self.line.split(",")

    def first_task(self) -> int:
        id_spans = [IDSpan(span) for span in self.parse_input()]
        invalid_ids = [span.sieve_invalid_ids() for span in id_spans]
        to_sum = chain.from_iterable(invalid_ids)
        return sum(to_sum)


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()