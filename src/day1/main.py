from pathlib import Path

class SafeWithDial:
    def __init__(self, pointing_at: int = 50):
        self.dial_number = pointing_at

    def rotate_left(self, degrees: int):
        return SafeWithDial(pointing_at=((self.dial_number - degrees) % 100))

    def rotate_right(self, degrees: int):
        return SafeWithDial(pointing_at=((self.dial_number + degrees) % 100))

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
