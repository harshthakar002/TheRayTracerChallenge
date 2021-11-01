from typing import List
from features.equality import EPSILON
from features.point import Point
from features.vector import Vector
from figures.figure import Figure
from figures.ray import Ray

class Plane(Figure):

    def __init__(self):
        super().__init__()

    def local_normal_at(self, point: Point) -> Vector:
        return Vector(0, 1, 0)
    
    def local_intersection_distance(self, ray: Ray) -> List[float]:
        if abs(ray.direction.y) < EPSILON:
            return []
        return [-ray.origin.y / ray.direction.y]