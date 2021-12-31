from features.point import Point
from features.vector import Vector
from figures.group import Group
from figures.triangle import Triangle
from math import inf


class ParsedObj():

    def __init__(self) -> None:
        self.processed = 0
        self.ignored = 0
        self.vertices = [Point(-inf, -inf, -inf)]
        self.groups = [Group()]
        self.normals = [Vector(-inf, -inf, -inf)]
    

    def ignore(self) -> None:
        self.ignored += 1

    def add_vertex(self, x: float, y: float, z: float) -> None:
        self.vertices.append(Point(x, y, z))
    
    def add_normal(self, x: float, y: float, z: float) -> None:
        self.normals.append(Vector(x, y, z))

    def add_triangle(self, index1: int, index2: int, index3: int) -> None:
        triangle = Triangle(self.vertices[index1], self.vertices[index2], self.vertices[index3])
        self.groups[-1].add_child(triangle)

    def add_group(self, name: str) -> None:
        self.groups.append(Group(name))

    def mark_processed(self) -> None:
        self.processed += 1

    def asGroup(self) -> Group:
        parsed_obj_group = Group()
        for group in self.groups:
            if len(group.shapes) > 0:
                parsed_obj_group.add_child(group)
        return parsed_obj_group