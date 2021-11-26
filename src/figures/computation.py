from figures.figure import Figure
from features.point import Point
from features.vector import Vector
from features.equality import EPSILON

class Computation():

    def __init__(self, t: float, object: Figure, point: Point, eyev: Vector, normalv: Vector, ray_to_be_reflected: Vector, n1: float, n2: float) -> None:
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
        self.reflectv = ray_to_be_reflected.reflect(self.normalv)
        self.over_point = Point.fromTuple(self.point + (self.normalv * EPSILON))
        self.under_point = Point.fromTuple(self.point - (self.normalv * EPSILON))
        self.n1 = n1
        self.n2 = n2
    