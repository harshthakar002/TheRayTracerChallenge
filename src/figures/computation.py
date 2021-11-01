from figures.figure import Figure
from features.point import Point
from features.vector import Vector
from features.equality import EPSILON

class Computation():

    def __init__(self, t: float, object: Figure, point: Point, eyev: Vector, normalv: Vector) -> None:
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev
        if normalv.dotProduct(eyev) < 0:
            self.inside = True
            self.normalv = normalv.negate()
        else:
            self.inside = False
            self.normalv = normalv
        self.over_point = Point.fromTuple(self.point + (self.normalv * EPSILON))
    