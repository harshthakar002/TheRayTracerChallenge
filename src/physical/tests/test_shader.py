from features.color import Color
from physical.shader import Shader
from physical.material import Material
from features.point import Point
from physical.point_light import PointLight
from features.vector import Vector
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