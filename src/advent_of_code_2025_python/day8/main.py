import heapq
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Counter, Iterable

from scipy.spatial import cKDTree


@dataclass(frozen=True)
class JBox:
    x: int
    y: int
    z: int

    @staticmethod
    def from_string(string: str) -> JBox:
        pattern = re.compile(r"\d+")
        coords = re.findall(pattern, string)
        assert len(coords) == 3, f"Not enough coordinates from {string=}"
        return JBox(*[int(coord) for coord in coords])

    @property
    def coords(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)


def add_new_pair(
    circuits: Counter[frozenset[int]],
    connected: set[int],
    left: int,
    right: int,
) -> None:
    pair = frozenset([left, right])
    connected.update(pair)
    key_to_delete = None
    for key in circuits.keys():
        if left in key or right in key:
            key_to_delete = key
            new_key = frozenset({*key, *pair})
            circuits[new_key] = len(new_key)
    else:
        connected.update(pair)
        circuits[pair] = 2
    if key_to_delete is not None:
        del circuits[key_to_delete]

def extend_one_circuit(
    circuits: Counter[frozenset[int]],
    present_element: int,
    missing_element: int
) -> None:
    key_to_delete = None
    for keyset in circuits.keys():
        if present_element in keyset:
            key_to_delete = keyset
            crowd = frozenset({*keyset, missing_element})
            circuits[crowd] = len(crowd)
            break
    del circuits[key_to_delete]


def merge_two_circuits(
    circuits: Counter[frozenset[int]],
    left: int,
    right: int,
):
    left_key, right_key = None, None
    for keyset in circuits.keys():
        if left in keyset:
            left_key = keyset
        if right in keyset:
            right_key = keyset
    if left_key == right_key:
        return None
    new_key = frozenset({*left_key,  *right_key})
    circuits[new_key] = len(new_key)
    del circuits[left_key]
    del circuits[right_key]


class PlayGround:
    def __init__(self, lines: list[str]):
        self.jboxes: list[JBox] = [JBox.from_string(line) for line in lines]

    def find_n_closest_pair_indices(self, number_of_pairs: int) -> Iterable[tuple[int, int]]:
        vectors = [jbox.coords for jbox in self.jboxes]
        max_rank = len(vectors)
        self.neighbors = cKDTree(vectors)
        distances, indices = self.neighbors.query(vectors, k=max_rank+1)
        paired_distance = {}
        for i in range(max_rank):
            for rank in range(1, max_rank+1):
                j = int(indices[i, rank])
                key = (min(i,j), max(i,j))
                distance = distances[i, rank]
                if key not in paired_distance:
                    paired_distance[key] = distance
        return heapq.nsmallest(number_of_pairs, paired_distance.keys(), key=paired_distance.get)


    def circuit_counter(self, connections: int) -> Counter[frozenset[int]]:
        connected: set[int] = set()
        circuits: Counter[frozenset[int]] = Counter()
        for i, j in self.find_n_closest_pair_indices(connections):
            if len(connected) == 0:
                add_new_pair(circuits, connected, i, j)
            elif i not in connected and j not in connected:
                add_new_pair(circuits, connected, i, j)
            elif i in connected and j not in connected:
                extend_one_circuit(circuits, i, j)
                connected.add(j)
            elif i not in connected and j in connected:
                extend_one_circuit(circuits, j, i)
                connected.add(i)
            else:
                merge_two_circuits(circuits, i, j)
        return circuits


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self, connections=10) -> int:
        playground = PlayGround(self.lines)
        circuits = playground.circuit_counter(connections)
        return math.prod(length for _, length in circuits.most_common(3))


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task(1000))
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()