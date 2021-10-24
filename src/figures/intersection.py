from __future__ import annotations
from figures.ray import Ray
from figures.figure import Figure
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
