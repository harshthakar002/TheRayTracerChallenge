from typing import List
from features.bounds import Bounds
from features.equality import EPSILON
from features.point import Point
from features.vector import Vector
from figures.shape import Shape
from figures.ray import Ray
from math import inf

class Plane(Shape):

    def __init__(self):
        super().__init__()

    def local_normal_at(self, point: Point, u: float, v: float) -> Vector:
        return Vector(0, 1, 0)
    
    def local_intersection_distance(self, ray: Ray) -> List[tuple[float, float, float]]:
        if abs(ray.direction.y) < EPSILON:
            return []
        return [(-ray.origin.y / ray.direction.y, None, None)]
    
    def bounds(self) -> Bounds:
        return Bounds(-inf, 0, -inf, inf, 0, inf)