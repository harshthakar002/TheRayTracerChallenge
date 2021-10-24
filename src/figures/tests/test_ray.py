from figures.ray import Ray
from features.point import Point
from features.vector import Vector

def test_ray_creation():
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)
    ray = Ray(origin, direction)
    assert ray.origin == origin
    assert ray.direction == direction