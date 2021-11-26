from figures.shape import Shape
from features.point import Point
from features.vector import Vector
from features.equality import EPSILON
from math import sqrt

class Computation():

    def __init__(self, t: float, object: Shape, point: Point, eyev: Vector, normalv: Vector, ray_to_be_reflected: Vector, n1: float, n2: float) -> None:
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
    
    def schlick(self) -> float:
        cos = self.eyev.dotProduct(self.normalv)
        if self.n1 > self.n2:
            n = self.n1 / self.n2
            sin2_t = (n*n) * (1.0 - (cos * cos))
            if sin2_t > 1.0:
                return 1.0
            cos_t = sqrt(1.0 - sin2_t)
            cos = cos_t
        r0 = pow((self.n1 - self.n2) / (self.n1 + self.n2), 2)
        return r0 + ((1 - r0) * pow(1 - cos, 5))