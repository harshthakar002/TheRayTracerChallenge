from typing import List
from features.bounds import Bounds
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from figures.shape import Shape
from features.equality import EPSILON, is_approximately_equal
from math import sqrt, inf

class Cylinder(Shape):

    def __init__(self, minimum: float = -inf, maximum: float = inf, closed: bool = False):
        self.minimum = minimum
        self.maximum = maximum
        self.closed = closed
        super().__init__()
    
    def local_intersection_distance(self, ray: Ray) -> List[tuple[float, float, float]]:
        a = (ray.direction.x * ray.direction.x) + (ray.direction.z * ray.direction.z)
        if is_approximately_equal(a, 0.0):
            return self.intersect_caps(ray, [])
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
            ts.append((t0, None, None))
        
        y1 = ray.origin.y + (t1 * ray.direction.y)
        if self.minimum < y1 and y1 < self.maximum:
            ts.append((t1, None, None))
        return self.intersect_caps(ray, ts)
    
    @staticmethod
    def check_cap(ray: Ray, t: float):
        x = ray.origin.x + (t * ray.direction.x)
        z = ray.origin.z + (t * ray.direction.z)
        return ((x * x) + (z * z)) <= 1
    
    def intersect_caps(self, ray: Ray, ts: List[float]) -> List[tuple[float, float, float]]:
        if not self.closed or is_approximately_equal(ray.direction.y, 0):
            return ts
        t = (self.minimum - ray.origin.y) / ray.direction.y
        if Cylinder.check_cap(ray, t):
            ts.append((t, None, None))
        
        t = (self.maximum - ray.origin.y) / ray.direction.y
        if Cylinder.check_cap(ray, t):
            ts.append((t, None, None))
        return ts
        
    def local_normal_at(self, point: Point) -> Vector:
        dist = (point.x * point.x) + (point.z * point.z)
        if dist < 1 and point.y >= (self.maximum - EPSILON):
            return Vector(0, 1, 0)
        elif dist < 1 and point.y <= (self.minimum + EPSILON):
            return Vector(0, -1, 0)
            
        return Vector(point.x, 0, point.z)

    def bounds(self) -> Bounds:
        return Bounds(-1, self.minimum, -1, 1, self.maximum, 1)