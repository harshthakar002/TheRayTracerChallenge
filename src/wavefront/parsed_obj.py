from features.point import Point
from figures.group import Group
from figures.triangle import Triangle
from math import inf


class ParsedObj():

    def __init__(self) -> None:
        self.processed = 0
        self.ignored = 0
        self.vertices = [Point(-inf, -inf, -inf)]
        self.default_group = Group()
    

    def ignore(self) -> None:
        self.ignored += 1

    def add_vertex(self, x: float, y: float, z: float) -> None:
        self.vertices.append(Point(x, y, z))

    def add_triangle(self, index1: int, index2: int, index3: int) -> None:
        triangle = Triangle(self.vertices[index1], self.vertices[index2], self.vertices[index3])
        self.default_group.add_child(triangle)

    def mark_processed(self) -> None:
        self.processed += 1