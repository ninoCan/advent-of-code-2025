from pathlib import Path



class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

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
