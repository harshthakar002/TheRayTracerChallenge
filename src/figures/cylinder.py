from typing import List
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from figures.shape import Shape
from features.equality import is_approximately_equal
from math import sqrt, inf

class Cylinder(Shape):

    def __init__(self, minimum: float = -inf, maximum: float = inf, closed: bool = False):
        self.minimum = minimum
        self.maximum = maximum
        self.closed = closed
        super().__init__()
    
    def local_intersection_distance(self, ray: Ray) -> List[float]:
        a = (ray.direction.x * ray.direction.x) + (ray.direction.z * ray.direction.z)
        if is_approximately_equal(a, 0.0):
            return []
        b = (2 * ray.origin.x * ray.direction.x) + (2 * ray.origin.z * ray.direction.z)
        c = (ray.origin.x * ray.origin.x) + (ray.origin.z * ray.origin.z) - 1
        disc = (b * b) - (4 * a * c)
        if disc < 0:
            return []
        
        t0 = (-b - sqrt(disc)) / (2 * a)
        t1 = (-b + sqrt(disc)) / (2 * a)
        if t0 > t1:
            t0, t1 = t1, t0
        ts = []
        y0 = ray.origin.y + (t0 * ray.direction.y)
        if self.minimum < y0 and y0 < self.maximum:
            ts.append(t0)
        
        y1 = ray.origin.y + (t1 * ray.direction.y)
        if self.minimum < y1 and y1 < self.maximum:
            ts.append(t1)
        return ts

    def local_normal_at(self, point: Point) -> Vector:
        return Vector(point.x, 0, point.z)