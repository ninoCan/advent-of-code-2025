import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import networkx as nx


@dataclass(frozen=True)
class Device:
    label: str
    outputs: list[str]

    def from_str(s: str) -> Device:
        pattern = re.compile(r"\b[a-z]{3}\b")
        label, output_bit = s.split(":")
        outputs = re.findall(pattern, output_bit)
        return Device(label, outputs)

type DeviceLabel = Device.label

class ServerRack:
    def __init__(
        self,
        lines: list[str],
    ):
        self.devices = [
            Device.from_str(line) for line in lines
        ]
        self.routes = self._generate_routes()

    def _generate_routes(self) -> nx.DiGraph:
        routes = nx.DiGraph()
        for device in self.devices:
            routes.add_edges_from([(device.label, dest) for dest in device.outputs])
        return routes



class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        server = ServerRack(self.lines)
        return sum(
            1
            for _ in nx.all_simple_paths(
                server.routes,
                source="you",
                target="out",
            )
        )



    def second_task(self) -> int:
        server = ServerRack(self.lines)
        visited : Counter[list[str]] =Counter()
        for path in nx.all_simple_paths(
            server.routes,
            source="svr",
            target="out",
        )
        return sum(
            1
            for path in nx.all_simple_paths(
                server.routes,
                source="svr",
                target="out",
            )
            if "dac" in path and "fft" in path
        )

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()