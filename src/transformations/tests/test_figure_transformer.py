from figures.ray import Ray
from features.point import Point
from features.vector import Vector
from transformations.figure_transformer import FigureTransformer

def test_translating_ray():
    ray = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    origin_m, direction_m = FigureTransformer.translation(3, 4, 5)
    translated_ray = ray.get_transformed_ray(origin_m, direction_m)
    assert translated_ray.origin == Point(4, 6, 8)
    assert translated_ray.direction == Vector(0, 1, 0)

def test_scaling_ray():
    ray = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    origin_m, direction_m = FigureTransformer.scaling(2, 3, 4)
    translated_ray = ray.get_transformed_ray(origin_m, direction_m)
    assert translated_ray.origin == Point(2, 6, 12)
    assert translated_ray.direction == Vector(0, 3, 0)