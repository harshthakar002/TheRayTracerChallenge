from typing import List
from features.bounds import Bounds
from features.equality import EPSILON
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from figures.shape import Shape

class Triangle(Shape):

    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.e1 = Vector.fromtuple(self.p2 - self.p1)
        self.e2 = Vector.fromtuple(self.p3 - self.p1)
        self.normal = self.e2.crossProduct(self.e1).normalize()
    
    def local_normal_at(self, point: Point) -> Vector:
        return self.normal

    def local_intersection_distance(self, ray: Ray) -> List[float]:
        dir_cross_e2 = Vector.fromtuple(ray.direction).crossProduct(self.e2)
        det = self.e1.dotProduct(dir_cross_e2)
        if abs(det) < EPSILON:
            return []
        f = 1.0 / det
        p1_to_origin = ray.origin - self.p1
        u = f * p1_to_origin.dotProduct(dir_cross_e2)
        if u < 0 or u > 1:
            return []
        origin_cross_e1 = Vector.fromtuple(p1_to_origin).crossProduct(self.e1)
        v = f * ray.direction.dotProduct(origin_cross_e1)
        if v < 0 or (u + v) > 1:
            return []
        return [f * self.e2.dotProduct(origin_cross_e1)]
    
    def bounds(self) -> Bounds:
        return Bounds(min(self.p1.x, self.p2.x, self.p3.x),
                      min(self.p1.y, self.p2.y, self.p3.y),
                      min(self.p1.z, self.p2.z, self.p3.z),
                      max(self.p1.x, self.p2.x, self.p3.x),
                      max(self.p1.y, self.p2.y, self.p3.y),
                      max(self.p1.z, self.p2.z, self.p3.z))