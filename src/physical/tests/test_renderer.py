from features.color import Color
from features.point import Point
from features.vector import Vector
from physical.camera import Camera
from physical.renderer import Renderer
from physical.default_world import DefaultWorld
from transformations.view_transformer import ViewTransformer
from math import pi

def test_rendering_world_with_camera():
    w = DefaultWorld()
    from_point = Point(0, 0, -5)
    to_point = Point(0, 0, 0)
    up = Vector(0, 1, 0)
    c = Camera(11, 11, pi / 2, ViewTransformer.view_transform(from_point, to_point, up))
    image = Renderer.render(c, w)
    assert image.pixel_at(5, 5) == Color(0.38066, 0.47583, 0.2855)