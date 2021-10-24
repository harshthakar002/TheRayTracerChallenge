from features.color import Color
from features.point import Point
from physical.point_light import PointLight

def test_point_light_creation():
    intensity = Color(1, 1, 1)
    position = Point(0, 0, 0)
    light = PointLight(intensity, position)
    assert light.intensity == intensity
    assert light.position == position