from math import pi, sqrt
from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from physical.camera import Camera
from transformations.transformer import Transformer

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

def test_construct_ray_through_center_of_the_canvas():
    c = Camera(201, 101, pi / 2)
    r = Ray.ray_for_pixel(c, 100, 50)
    assert r.origin == Point(0, 0, 0)
    assert r.direction == Vector(0, 0, -1)

def test_construct_ray_through_corner_of_the_canvas():
    c = Camera(201, 101, pi / 2)
    r = Ray.ray_for_pixel(c, 0, 0)
    assert r.origin == Point(0, 0, 0)
    assert r.direction == Vector(0.66519, 0.33259, -0.66851)

def test_construct_ray_when_camera_is_transformed():
    tranformation = Transformer.rotation_y(pi / 4).multiply_matrices(Transformer.translation(0, -2, 5))
    c = Camera(201, 101, pi / 2, tranformation)
    r = Ray.ray_for_pixel(c, 100, 50)
    assert r.origin == Point(0, 2, -5)
    assert r.direction == Vector(sqrt(2) / 2, 0, -sqrt(2) / 2)
