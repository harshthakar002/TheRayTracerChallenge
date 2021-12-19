from __future__ import annotations
from features.point import Point

class Bounds():

    def __init__(self, min_x: float, min_y: float, min_z: float, max_x: float, max_y: float, max_z: float) -> None:
        if min_x > max_x or min_y > max_y or min_z > max_z:
            raise ValueError('min value cannpt be greater than max value')
        self.min_point = Point(min_x, min_y, min_z)
        self.max_point = Point(max_x, max_y, max_z)
    
    def __eq__(self, bounds: Bounds) -> bool:
        return self.min_point == bounds.min_point and self.max_point == bounds.max_point