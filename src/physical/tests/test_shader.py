from features.color import Color
from physical.shader import Shader
from physical.material import Material
from features.point import Point
from physical.point_light import PointLight
from features.vector import Vector
from physical.default_world import DefaultWorld
from figures.ray import Ray
from figures.intersection import Intersection
from math import sqrt

def test_lighting_with_eye_between_light_and_surface():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, -10))
    result = Shader.lighting(m, light, position, eyev, normalv)
    assert result == Color(1.9, 1.9, 1.9)

def test_lighting_with_eye_between_light_and_surface_at_45():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, sqrt(2) / 2, -sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, -10))
    result = Shader.lighting(m, light, position, eyev, normalv)
    assert result == Color(1.0, 1.0, 1.0)

def test_lighting_with_eye_opposite_surface_at_45():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 10, -10))
    result = Shader.lighting(m, light, position, eyev, normalv)
    assert result == Color(0.7364, 0.7364, 0.7364)

def test_lighting_with_eye_in_path_of_reflection():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, -sqrt(2) / 2, -sqrt(2) / 2)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 10, -10))
    result = Shader.lighting(m, light, position, eyev, normalv)
    assert result == Color(1.6364, 1.6364, 1.6364)

def test_lighting_with_light_behind_surface():
    m = Material()
    position = Point(0, 0, 0)
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = PointLight(Color(1, 1, 1), Point(0, 0, 10))
    result = Shader.lighting(m, light, position, eyev, normalv)
    assert result == Color(0.1, 0.1, 0.1)

def test_shading_an_intersection():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = w.objects[0]
    i = Intersection(4, shape)
    comps = i.prepare_computation(r)
    c = Shader.shade_hit(w, comps)
    assert c == Color(0.38066, 0.47583, 0.2855)

def test_shading_an_intersection_from_inside():
    w = DefaultWorld()
    w.light = PointLight(Color(1, 1, 1), Point(0, 0.25, 0))
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = w.objects[1]
    i = Intersection(0.5, shape)
    comps = i.prepare_computation(r)
    c = Shader.shade_hit(w, comps)
    assert c == Color(0.90498, 0.90498, 0.90498)

def test_color_when_ray_misses():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
    c = Shader.color_at(w, r)
    assert c == Color(0, 0, 0)

def test_color_when_ray_hits():
    w = DefaultWorld()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    c = Shader.color_at(w, r)
    assert c == Color(0.38066, 0.47583, 0.2855)

def test_color_when_intersection_behind_ray():
    w = DefaultWorld()
    outer = w.objects[0]
    outer.material.ambient = 1
    inner = w.objects[1]
    inner.material.ambient = 1
    r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    c = Shader.color_at(w, r)
    assert c == inner.material.color