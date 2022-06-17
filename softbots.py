from __future__ import annotations
from softbodies import Node, Link


class Softbot:
    nodes: list[Node]
    links: list[Link]
    muscles: list[Muscle]

    def __init__(self, nodes: list[Node], links: list[Link], muscles: list[Muscle]) -> None:
        self.nodes = nodes
        self.links = links
        self.muscles = muscles


class Muscle(Link):
    length_original: float

    def __init__(self, nodes: tuple[Node, Node], stiffness: float, dampening: float, length: float = None) -> None:
        super().__init__(nodes, stiffness, dampening, length)
        self.length_original = length

    def set_length(self, activation) -> None:
        self.length = self.length_original * min(max((1 - 0.5 * activation), 0), 1)
