from copy import deepcopy
from pathlib import Path
from typing import Optional, List


class BatteryBank:

    def __init__(self, line: str):
        self.batteries = [int(item) for item in line]
        self.max_index = len(self.batteries) - 1

    @property
    def max_joltage(self) -> int:
        max1 = max(self.batteries)
        index1 = self.batteries.index(max1)
        if index1 == self.max_index:
            max2 = max(self.batteries[:index1] + self.batteries[index1 + 1:])
            return int(f"{max2}{max1}")
        sub_max = max(self.batteries[index1+1:])
        return int(f"{max1}{sub_max}")


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        banks = [BatteryBank(line.strip("\n")) for line in self.lines]
        return sum([bank.max_joltage for bank in banks])


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()