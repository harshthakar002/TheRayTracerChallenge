from features.color import Color, WHITE_COLOR, BLACK_COLOR
from physical.shader import Shader
from physical.material import Material
from features.point import Point
from physical.point_light import PointLight
from features.vector import Vector
from physical.default_world import DefaultWorld
from physical.world import World
from figures.ray import Ray
from figures.intersection import Intersection
from figures.sphere import Sphere
from transformations.figure_transformer import FigureTransformer
from math import sqrt
from patterns.stripe_pattern import StripePattern
from patterns.solid_pattern import SolidPattern
from patterns.test_pattern import TestPattern
from figures.plane import Plane

def test_lighting_with_eye_between_light_and_surface():
    m = Material()
    s = Sphere()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, -10))
    result = Shader.lighting(m, s, light, position, eyev, normalv, False)
    assert result == Color(1.9, 1.9, 1.9)

def test_lighting_with_eye_between_light_and_surface_at_45():
    m = Material()
    s = Sphere()
    position = Point(0, 0, 0)
    eyev = Vector(0, sqrt(2) / 2, -sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, -10))
    result = Shader.lighting(m, s, light, position, eyev, normalv, False)
    assert result == Color(1.0, 1.0, 1.0)

def test_lighting_with_eye_opposite_surface_at_45():
    m = Material()
    s = Sphere()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 10, -10))
    result = Shader.lighting(m, s, light, position, eyev, normalv, False)
    assert result == Color(0.7364, 0.7364, 0.7364)

def test_lighting_with_eye_in_path_of_reflection():
    m = Material()
    s = Sphere()
    position = Point(0, 0, 0)
    eyev = Vector(0, -sqrt(2) / 2, -sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 10, -10))
    result = Shader.lighting(m, s, light, position, eyev, normalv, False)
    assert result == Color(1.6364, 1.6364, 1.6364)

def test_lighting_with_light_behind_surface():
    m = Material()
    s = Sphere()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, 10))
    result = Shader.lighting(m, s, light, position, eyev, normalv, False)
    assert result == Color(0.1, 0.1, 0.1)

def test_shading_an_intersection():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = w.objects[0]
    i = Intersection(4, shape)
    comps = i.prepare_computation(r, [i])
    c = Shader.shade_hit(w, comps, 1)
    assert c == Color(0.38066, 0.47583, 0.2855)

def test_shading_an_intersection_from_inside():
    w = DefaultWorld()
    w.light = PointLight(Color(1, 1, 1), Point(0, 0.25, 0))
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = w.objects[1]
    i = Intersection(0.5, shape)
    comps = i.prepare_computation(r, [i])
    c = Shader.shade_hit(w, comps, 1)
    assert c == Color(0.90498, 0.90498, 0.90498)

def test_color_when_ray_misses():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
    c = Shader.color_at(w, r, 1)
    assert c == Color(0, 0, 0)

def test_color_when_ray_hits():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    c = Shader.color_at(w, r, 1)
    assert c == Color(0.38066, 0.47583, 0.2855)

def test_color_when_intersection_behind_ray():
    w = DefaultWorld()
    outer = w.objects[0]
    outer.material.ambient = 1
    inner = w.objects[1]
    inner.material.ambient = 1
    r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    c = Shader.color_at(w, r, 1)
    assert c == inner.material.color

def test_lighting_with_surface_in_shadow():
    m = Material()
    s = Sphere()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, -10))
    in_shadow = True
    result = Shader.lighting(m, s, light, position, eyev, normalv, in_shadow)
    assert result == Color(0.1, 0.1, 0.1)

def test_no_shadow_when_nothing_is_collinear_with_point_and_light():
    w = DefaultWorld()
    p = Point(0, 10, 0)
    assert not Shader.is_shadowed(w, p)

def test_shadow_when_object_between_point_and_light():
    w = DefaultWorld()
    p = Point(10, -10, 10)
    assert Shader.is_shadowed(w, p)

def test_no_shadow_when_object_behind_light():
    w = DefaultWorld()
    p = Point(-20, 20,-20)
    assert not Shader.is_shadowed(w, p)

def test_no_shadow_when_object_behind_point():
    w = DefaultWorld()
    p = Point(-2, 2, -2)
    assert not Shader.is_shadowed(w, p)

def test_shade_hit_is_given_an_intersection_in_shadow():
    w = World()
    w.light = PointLight(Color(1, 1, 1), Point(0, 0, -10))
    s1 = Sphere()
    s2 = Sphere()
    origin_transform, direction_transform = FigureTransformer.translation(0, 0, 10)
    s2.set_transform(origin_transform, direction_transform)
    w.objects += [s1, s2]
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    i = Intersection(4, s2)
    comps = i.prepare_computation(r, [i])
    c = Shader.shade_hit(w, comps, 1)
    assert c == Color(0.1, 0.1, 0.1)

def test_lighting_with_pattern_applied():
    m = Material()
    s = Sphere()
    m.pattern = StripePattern(SolidPattern(WHITE_COLOR), SolidPattern(BLACK_COLOR))
    m.ambient = 1
    m.diffuse = 0
    m.specular = 0
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(WHITE_COLOR, Point(0, 0, -10))
    c1 = Shader.lighting(m, s, light, Point(0.9, 0, 0), eyev, normalv, False)
    c2 = Shader.lighting(m, s, light, Point(1.1, 0, 0), eyev, normalv, False)
    assert c1 == WHITE_COLOR
    assert c2 == BLACK_COLOR

def test_refracted_color_with_an_opaque_surface():
    w = DefaultWorld()
    shape = w.objects[0]
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = [Intersection(4, shape), Intersection(6, shape)]
    comps = xs[0].prepare_computation(r, xs)
    c = Shader.refracted_color(w, comps, 5)
    assert c == BLACK_COLOR

def test_refracted_color_at_maximum_recursive_depth():
    w = DefaultWorld()
    shape = w.objects[0]
    shape.material.transparency = 1.0
    shape.material.refractive_index = 1.5
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = [Intersection(4, shape), Intersection(6, shape)]
    comps = xs[0].prepare_computation(r, xs)
    c = Shader.refracted_color(w, comps, 0)
    assert c == BLACK_COLOR

def test_refracted_color_under_total_internal_reflection():
    w = DefaultWorld()
    shape = w.objects[0]
    shape.material.transparency = 1.0
    shape.material.refractive_index = 1.5
    r = Ray(Point(0, 0, sqrt(2) / 2), Vector(0, 1, 0))
    xs = [Intersection(-sqrt(2) / 2, shape), Intersection(sqrt(2) / 2, shape)]
    comps = xs[1].prepare_computation(r, xs)
    c = Shader.refracted_color(w, comps, 5)
    assert c == BLACK_COLOR

def test_refracted_color_with_refracted_ray():
    w = DefaultWorld()
    A = w.objects[0]
    A.material.ambient = 1.0
    A.material.pattern = TestPattern()
    B = w.objects[1]
    B.material.transparency = 1.0
    B.material.refractive_index = 1.5
    r = Ray(Point(0, 0, 0.1), Vector(0, 1, 0))
    xs = [Intersection(-0.9899, A), Intersection(-0.4899, B), Intersection(0.4899, B), Intersection(0.9899, A)]
    comps = xs[2].prepare_computation(r, xs)
    c = Shader.refracted_color(w, comps, 5)
    assert c == Color(0, 0.99888, 0.04722)

def test_reflected_color_for_non_reflective_material():
    w = DefaultWorld()
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = w.objects[1]
    shape.material.ambient = 1
    i = Intersection(1, shape)
    comps = i.prepare_computation(r, [i])
    color = Shader.reflected_color(w, comps, 1)
    assert color == BLACK_COLOR

def test_reflected_color_for_a_reflective_material():
    w = DefaultWorld()
    shape = Plane()
    origin_transform, direction_transform = FigureTransformer.translation(0, -1, 0)
    shape.set_transform(origin_transform, direction_transform)
    shape.material.reflective = 0.5
    w.objects.append(shape)
    r = Ray(Point(0, 0, -3), Vector(0, -sqrt(2) / 2, sqrt(2) / 2))
    i = Intersection(sqrt(2), shape)
    comps = i.prepare_computation(r, [i])
    color = Shader.reflected_color(w, comps, 1)
    assert color == Color(0.19033, 0.23791, 0.14274)

def test_shade_hit_with_reflective_material():
    w = DefaultWorld()
    shape = Plane()
    origin_transform, direction_transform = FigureTransformer.translation(0, -1, 0)
    shape.set_transform(origin_transform, direction_transform)
    shape.material.reflective = 0.5
    w.objects.append(shape)
    r = Ray(Point(0, 0, -3), Vector(0, -sqrt(2) / 2, sqrt(2) / 2))
    i = Intersection(sqrt(2), shape)
    comps = i.prepare_computation(r, [i])
    color = Shader.shade_hit(w, comps, 1)
    assert color == Color(0.87676, 0.92434, 0.82917)


def test_mutually_reflective_surfaces():
    w = World()
    w.light = PointLight(WHITE_COLOR, Point(0, 0, 0))
    lower = Plane()
    origin_transform, direction_transform = FigureTransformer.translation(0, -1, 0)
    lower.set_transform(origin_transform, direction_transform)
    lower.material.reflective = 1
    upper = Plane()
    origin_transform, direction_transform = FigureTransformer.translation(0, 1, 0)
    upper.set_transform(origin_transform, direction_transform)
    upper.material.reflective = 1
    w.objects = [lower, upper]
    r = Ray(Point(0, 0, 0), Vector(0, 1, 0))
    Shader.color_at(w, r, 4)

def test_reflective_color_at_maximum_depth():
    w = DefaultWorld()
    shape = Plane()
    origin_transform, direction_transform = FigureTransformer.translation(0, -1, 0)
    shape.set_transform(origin_transform, direction_transform)
    shape.material.reflective = 0.5
    w.objects.append(shape)
    r = Ray(Point(0, 0, -3), Vector(0, -sqrt(2) / 2, sqrt(2) / 2))
    i = Intersection(sqrt(2), shape)
    comps = i.prepare_computation(r, [i])
    color = Shader.reflected_color(w, comps, 0)
    assert color == BLACK_COLOR

def test_shade_hit_with_a_transparent_material():
    w = DefaultWorld()
    floor = Plane()
    origin_transform, direction_transform = FigureTransformer.translation(0, -1, 0)
    floor.set_transform(origin_transform, direction_transform)
    floor.material.transparency = 0.5
    floor.material.refractive_index = 1.5
    w.objects.append(floor)
    ball = Sphere()
    origin_transform, direction_transform = FigureTransformer.translation(0, -3.5, -0.5)
    ball.set_transform(origin_transform, direction_transform)
    ball.material.color = Color(1, 0, 0)
    ball.material.ambient = 0.5
    w.objects.append(ball)
    r = Ray(Point(0, 0, -3), Vector(0, -sqrt(2) / 2, sqrt(2) / 2))
    xs = [Intersection(sqrt(2), floor)]
    comps = xs[0].prepare_computation(r, xs)
    color = Shader.shade_hit(w, comps, 5)
    assert color == Color(0.93642, 0.68642, 0.68642)