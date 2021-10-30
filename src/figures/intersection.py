from __future__ import annotations
from figures.ray import Ray
from figures.figure import Figure
from physical.world import World
from figures.computation import Computation
from typing import List

class Intersection():

    def __init__(self, t: float, object: Figure) -> None:
        self.t = t
        self.object = object
    
    @staticmethod
    def find_intersections_of_ray_and_figure(ray: Ray, figure: Figure) -> List[Intersection]:
        intersection_distances = figure.ray_intersection_distance(ray)
        intersections = []
        for intersection_distance in intersection_distances:
            intersections.append(Intersection(intersection_distance, figure))
        return intersections
    
    @staticmethod
    def calculate_hit(intersections: List[Intersection]) -> Intersection:
        sorted_intersections = sorted(intersections, key=lambda student: student.t)
        for intersection in sorted_intersections:
            if intersection.t >= 0:
                return intersection
        return None
    
    @staticmethod
    def find_intersections_of_ray_and_world(ray: Ray, world: World) -> List[Intersection]:
        intersections = []
        for object in world.objects:
            intersections = intersections + Intersection.find_intersections_of_ray_and_figure(ray, object)
        return sorted(intersections, key=lambda intersection: intersection.t)

    @staticmethod
    def prepare_computation(intersection: Intersection, ray: Ray) -> Computation:
        point = ray.position(intersection.t)
        return Computation(intersection.t, intersection.object, point, ray.direction.negate(), intersection.object.normal_at(point))
