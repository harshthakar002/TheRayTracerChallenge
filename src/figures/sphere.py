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
    
    def ray_intersection_distance(self, ray: Ray) -> List[float]:
        transformed_ray = ray.get_transformed_ray(self.ray_origin_transform, self.ray_direction_transform)
        sphere_to_ray = transformed_ray.origin - self.origin
        a = transformed_ray.direction.dotProduct(transformed_ray.direction)
        b = 2 * transformed_ray.direction.dotProduct(sphere_to_ray)
        c = sphere_to_ray.dotProduct(sphere_to_ray) - 1
        discriminant = (b*b) - (4 * a * c)
        if discriminant < 0:
            return []
        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)
        return [t1, t2]
