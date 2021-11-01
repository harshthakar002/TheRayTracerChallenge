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
        if (magnitude == 0):
            return self
        return Vector(self.x / magnitude, self.y / magnitude, self.z / magnitude)

    def crossProduct(self, v: Vector) -> Vector:
        return Vector((self.y * v.z) - (self.z * v.y), (self.z * v.x) - (self.x * v.z), (self.x * v.y) - (self.y * v.x))
    
    def reflect(self, normal: Vector) -> Vector:
        reflection = self - (normal * 2 * self.dotProduct(normal))
        return Vector(reflection.x, reflection.y, reflection.z)
    
    def negate(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    @staticmethod
    def fromtuple(t: Tuple) -> Vector:
        if not t.is_vector():
            raise TypeError('Cannot convert non-vector tuple to vector')
        return Vector(t.x, t.y, t.z)

ZERO_VECTOR = Vector(0, 0, 0)
