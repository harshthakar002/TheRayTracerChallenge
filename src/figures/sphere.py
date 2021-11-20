from typing import List
from features.point import Point
from features.vector import Vector
from figures.figure import Figure
from figures.ray import Ray 
from features.equality import is_approximately_equal
from math import sqrt

class Sphere(Figure):

    def __init__(self):
        self.origin = Point(0, 0, 0)
        self.radius = 1
        super().__init__()
    
    def local_intersection_distance(self, ray: Ray) -> List[float]:
        sphere_to_ray = ray.origin - self.origin
        a = ray.direction.dotProduct(ray.direction)
        b = 2 * ray.direction.dotProduct(sphere_to_ray)
        c = sphere_to_ray.dotProduct(sphere_to_ray) - 1
        discriminant = (b*b) - (4 * a * c)
        if discriminant < 0:
            return []
        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)
        return [t1, t2]
    
    def local_normal_at(self, point: Point) -> Vector:
        return Vector.fromtuple(point - Point(0, 0, 0))

class GlassSphere(Sphere):

    def __init__(self):
        super().__init__()
        self.material.transparency = 1.0
        self.material.refractive_index = 1.5