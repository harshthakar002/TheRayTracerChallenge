from physical.light import Light
from features.point import Point
from features.color import Color

def test_light_creation():
    intensity = Color(1, 1, 1)
    position = Point(1, 2, 3)
    light = Light(intensity, position)
    assert light.position == position
    assert light.intensity == intensity

def test_light_equality():
    light = Light(Color(1, 1, 1), Point(1, 2, 3))
    assert light == Light(Color(1, 1, 1), Point(1, 2, 3))