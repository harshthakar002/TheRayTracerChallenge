from features.point import Point
from math import inf


class ParsedObj():

    def __init__(self) -> None:
        self.processed = 0
        self.ignored = 0
        self.vertices = [Point(-inf, -inf, -inf)]
    

    def ignore(self) -> None:
        self.ignored += 1

    def add_vertex(self, x: float, y: float, z: float) -> None:
        self.vertices.append(Point(x, y, z))
        self.processed += 1    