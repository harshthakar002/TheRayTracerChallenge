from typing import List
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
        div_cross_e2 = Vector.fromtuple(ray.direction).crossProduct(self.e2)
        det = self.e1.dotProduct(div_cross_e2)
        if abs(det) < EPSILON:
            return []
        
        return [1]