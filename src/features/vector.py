from __future__ import annotations
from features.tuple import tuple
import math


class vector(tuple):
    def __init__(self, x: float, y: float, z: float) -> None:
        super().__init__(x, y, z, 0.0)

    def magnitude(self) -> float:
        return math.sqrt((self.x*self.x) + (self.y*self.y) + (self.z*self.z))

    def normalize(self) -> vector:
        magnitude = self.magnitude()
        return vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def dotProduct(self, v: vector) -> float:
        return (self.x * v.x) + (self.y * v.y) + (self.z * v.z)

    def crossProduct(self, v: vector) -> vector:
        return vector((self.y * v.z) - (self.z * v.y), (self.z * v.x) - (self.x * v.z), (self.x * v.y) - (self.y * v.x))


ZERO_VECTOR = vector(0, 0, 0)
