from __future__ import annotations
from features.tuple import Tuple
import math


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 0.0)

    def magnitude(self) -> float:
        return math.sqrt((self.x*self.x) + (self.y*self.y) + (self.z*self.z))

    def normalize(self) -> Vector:
        magnitude = self.magnitude()
        return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def crossProduct(self, v: Vector) -> Vector:
        return Vector((self.y * v.z) - (self.z * v.y), (self.z * v.x) - (self.x * v.z), (self.x * v.y) - (self.y * v.x))


ZERO_VECTOR = Vector(0, 0, 0)
