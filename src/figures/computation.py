from figures.figure import Figure
from features.point import Point
from features.vector import Vector

class Computation():

    def __init__(self, t: float, object: Figure, point: Point, eyev: Vector, normalv: Vector) -> None:
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev
        self.normalv = normalv
    