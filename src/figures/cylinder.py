from typing import List
from figures.ray import Ray
from figures.shape import Shape
from features.equality import is_approximately_equal
from math import sqrt

class Cylinder(Shape):

    def __init__(self):
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
        return [t0, t1]