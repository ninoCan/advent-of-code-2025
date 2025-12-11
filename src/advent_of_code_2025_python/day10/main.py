import logging
import re
from copy import deepcopy
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Optional

import numpy as np

type MachineProps = tuple[str, list[list[int]], list[int]]

class Machine:
    light_diagram: str
    buttons: list[list[int]]
    joltage_reqs: list[int]

    def __init__(
        self,
        diagram: str,
        buttons: list[list[int]],
        joltage_reqs: list[int],
    ):
        self.light_diagram = diagram
        self.buttons = buttons
        self.joltage_reqs = joltage_reqs
        self.key = int(
            self.light_diagram
            .replace(".", "0")
            .replace("#", "1"),
            2
        )
        length = len(self.light_diagram)
        self.operations = [
            sum([2**(length - 1 - light) for light in button])
            for button in self.buttons
        ]


    def minimal_buttons_to_turn_on(self, strategy: str = "depth-first") -> list[int]:
        if strategy != "depth-first":
            raise NotImplementedError(f"Strategy {strategy} was not implemented yet")
        return self._dfs_minimal_buttons()

    def _dfs_minimal_buttons(self) -> int:
        initial_state = 0
        button_pressed = 1
        state = initial_state
        while state != self.key:
            for combo in combinations_with_replacement(self.operations, button_pressed):
                for button in combo:
                    state = state ^ button
                if state == self.key:
                    return list(combo)
                state = initial_state
            else:
                button_pressed += 1
                if button_pressed == len(self.buttons) + 1:
                    logging.warning(f"WARNING: All possible states reached! Check your logic for {self.light_diagram}")
                    return []

    def minimal_buttons_to_reach_joltage_reqs(
        self,
        # strategy: str = "principal-value-decomposition",
        strategy: str = "deep-first"

    ) -> int:
        if strategy == "deep-first":
            return self._dfs_minimal_buttons_to_reach_joltages()
        if strategy != "principal-value-decomposition":
            raise NotImplementedError(f"Strategy {strategy} was not implemented yet")
        return self._pvd_minimal_buttons_to_reach_joltages()

    def _pvd_minimal_buttons_to_reach_joltages(self) -> int:
        vector = np.array(self.joltage_reqs)
        basis_vectors = []
        for button in self.buttons:
            state = [0] * len(self.joltage_reqs)
            for light in button:
                state[light] += 1
            basis_vectors.append(np.array(state))
        matrix = np.column_stack(basis_vectors)
        coefficients, residuals, rank, s = np.linalg.lstsq(matrix, vector, rcond=None)
        # A = np.array(basis_vectors)
        # b = np.array(vector)
        # coefficients = np.linalg.pinv(A) @ b
        # coefficients, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
        return sum(int(el) for el in coefficients)
        # matrix = np.column_stack(basis_vectors)
        # coefficients =np.linalg.solve(matrix, vector)
        # coefficients = np.linalg.pinv(matrix) @ vector
        # return sum(int(item) for item in coefficents)


    def _dfs_minimal_buttons_to_reach_joltages(self) -> int:
        initial_state = tuple([0] * len(self.joltage_reqs))
        button_pressed = 1
        state = list(initial_state)
        while state != self.key:
            for combo in combinations_with_replacement(self.buttons, button_pressed):
                for button in combo:
                    for light in button:
                        state[light] += 1
                if state == self.joltage_reqs:
                    print(f"Found {self.joltage_reqs}")
                    return button_pressed
                state = list(initial_state)
            else:
                button_pressed += 1


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            raw_lines = file.readlines() if not lines else lines
            self.lines = [
                line
                for line in raw_lines
                if line != ""
            ]

    @staticmethod
    def parse(line) -> MachineProps:
        main_pattern = re.compile(r"\[(.*?)]\s(.*)\s\{(.*?)\}")
        single_button_pattern = re.compile(r"\(.*?\)")
        light_pattern = re.compile(r"\d")
        joltage_pattern = re.compile(r"\d+")

        [diagram, button_string, req_string] = re.findall(main_pattern, line)[0]
        buttons = [
            [
                int(light)
                for light in re.findall(light_pattern, button)
             ]
            for button in re.findall(single_button_pattern, button_string)
        ]
        joltages = [
            int(item)
            for item in re.findall(joltage_pattern, req_string)
        ]
        return (diagram, buttons, joltages)

    def first_task(self) -> int:
        machines = [Machine(*self.parse(line)) for line in self.lines]
        return sum(len(machine.minimal_buttons_to_turn_on()) for machine in machines)


    def second_task(self) -> int:
        machines = [Machine(*self.parse(line)) for line in self.lines]
        return sum(machine.minimal_buttons_to_reach_joltage_reqs() for machine in machines)

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()