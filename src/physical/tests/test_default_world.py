from features.color import Color
from features.point import Point
from physical.default_world import DefaultWorld
from physical.point_light import PointLight

def test_default_world_creation():
    w = DefaultWorld()
    assert w.light_sources[0] == PointLight(Color(1, 1, 1), Point(-10, 10, -10))
    assert len(w.objects) == 2