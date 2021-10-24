from features.point import Point
from features.vector import Vector

class Ray():

    def __init__(self, origin: Point, direction: Vector) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, time: float) -> Point:
        return self.origin + (self.direction * time)