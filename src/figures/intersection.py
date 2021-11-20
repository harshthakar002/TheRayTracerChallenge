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
    def calculate_hit_from_sorted_intersections(sorted_intersections: List[Intersection]) -> Intersection:
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

    def prepare_computation(self, ray: Ray, xs: List[Intersection]) -> Computation:
        point = ray.position(self.t)
        containers: List[Figure] = []
        for intersection in xs:
            if intersection == self:
                if len(containers) == 0:
                    n1 = 1.0
                else:
                    n1 = containers[-1].material.refractive_index
            if intersection.object in containers:
                containers.remove(intersection.object)
            else:
                containers.append(intersection.object)
            
            if intersection == self:
                if len(containers) == 0:
                    n2 = 1.0
                else:
                    n2 = containers[-1].material.refractive_index
        return Computation(self.t, self.object, point, ray.direction.negate(), self.object.normal_at(point), n1, n2)
