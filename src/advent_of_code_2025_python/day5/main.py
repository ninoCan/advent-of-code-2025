from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import Optional, Counter


class Cafeteria:
    def __init__(
        self,
        freshness_ranges: list[str],
        raw_ingredients: list[str],
    ) -> None:

        self.freshness_ranges = [
            (int(low), int(high))
            for extent in freshness_ranges
            for low, high in [extent.split("-")]
            if "-" in extent
        ]
        self.raw_ingredients = [
           int(item)
           for item in raw_ingredients
           if item != ""
        ]

    @cached_property
    def status(self) -> dict[str, list[int]]:
        status = {
            "fresh": [],
            "spoiled": [],
        }
        for ingredient in self.raw_ingredients:
            if any(
                low <= ingredient <= high
                for extent in self.freshness_ranges
                for low, high in [extent]
            ):
                status["fresh"].append(ingredient)
            else:
                status["spoiled"].append(ingredient)
        return status

    @cached_property
    def number_of_fresh_ingredients(self) -> int:
        processed = Counter({
            (low, high): high - low + 1
            for [low, high] in self.freshness_ranges
        })
        for [low, high] in self.freshness_ranges:
            self.deduplicate_range(high, low, processed)
        return processed.total()

    def deduplicate_range(self, high: int, low: int, processed: Counter[tuple[int, int]]):
        pivot = deepcopy(processed)
        for [plow, phigh] in pivot.keys():
            if low > phigh or high < plow:
                processed[(low, high)] = high - low + 1
            elif plow <= low <= phigh < high:
                del processed[(plow, phigh)]
                del processed[(low, high)]
                processed[(plow, high)] = high - plow + 1
                low = plow
            elif low < plow <= high <= phigh:
                del processed[(plow, phigh)]
                del processed[(low, high)]
                processed[(low, phigh)] = phigh - low + 1
                high = phigh
            elif plow <= low <= high <= phigh:
                del processed[(low, high)]
                low, high = plow, phigh
            elif low <= plow <= phigh <= high:
                del processed[(plow, low)]
                del processed[(low, high)]
                processed[(low, high)] = high - low + 1
            else:
                raise RuntimeError("Something is askew with my logic")


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
        empty_index = self.lines.index("")
        cafeteria = Cafeteria(self.lines[:empty_index], self.lines[empty_index + 1:])
        return len(cafeteria.status['fresh'])


    def second_task(self) -> int:
        empty_index = self.lines.index("")
        cafeteria = Cafeteria(self.lines[:empty_index], self.lines[empty_index + 1:])
        return cafeteria.number_of_fresh_ingredients

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()