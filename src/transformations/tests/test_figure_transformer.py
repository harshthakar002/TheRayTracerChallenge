from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from transformations.transformer import Transformer

def test_translating_ray():
    ray = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    transform = Transformer.translation(3, 4, 5)
    translated_ray = ray.get_transformed_ray(transform)
    assert translated_ray.origin == Point(4, 6, 8)
    assert translated_ray.direction == Vector(0, 1, 0)

def test_scaling_ray():
    ray = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    transform = Transformer.scaling(2, 3, 4)
    sheared_ray = ray.get_transformed_ray(transform)
    assert sheared_ray.origin == Point(2, 6, 12)
    assert sheared_ray.direction == Vector(0, 3, 0)