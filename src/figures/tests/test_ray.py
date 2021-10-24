from figures.ray import Ray
from features.point import Point
from features.vector import Vector

def test_ray_creation():
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)
    ray = Ray(origin, direction)
    assert ray.origin == origin
    assert ray.direction == direction

def test_compute_point_from_a_distance():
    ray = Ray(Point(2, 3, 4), Vector(1, 0, 0))
    assert ray.position(0) == Point(2, 3, 4)
    assert ray.position(1) == Point(3, 3, 4)
    assert ray.position(-1) == Point(1, 3, 4)
    assert ray.position(2.5) == Point(4.5, 3, 4)