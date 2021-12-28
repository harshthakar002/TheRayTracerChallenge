from typing import List, Tuple
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from figures.shape import Shape
from features.equality import EPSILON
from math import inf

class Cube(Shape):

    def __init__(self):
        super().__init__()

    def local_intersection_distance(self, ray: Ray) -> List[tuple[float, float, float]]:
        xtmin, xtmax = Cube.check_axis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = Cube.check_axis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = Cube.check_axis(ray.origin.z, ray.direction.z)
        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)
        if tmin > tmax:
            return []
        
        return [(tmin, None, None), (tmax, None, None)]

    @staticmethod
    def check_axis(origin: float, direction:float) -> Tuple[float, float]:
        tmin_numerator = -1 - origin
        tmax_numerator = 1 - origin
        if abs(direction) >= EPSILON:
            tmin = tmin_numerator / direction
            tmax = tmax_numerator / direction
        else:
            tmin = tmin_numerator * inf
            tmax = tmax_numerator * inf
        
        if tmin > tmax:
            tmin, tmax = tmax, tmin
        return tmin, tmax
    
    def local_normal_at(self, point: Point, u: float, v: float) -> Vector:
        maxc = max(abs(point.x), abs(point.y), abs(point.z))
        if maxc == abs(point.x):
            return Vector(point.x, 0, 0)
        elif maxc == abs(point.y):
            return Vector(0, point.y, 0)
        return Vector(0, 0, point.z)