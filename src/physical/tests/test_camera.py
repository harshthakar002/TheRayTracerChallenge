from physical.camera import Camera
from features.equality import is_approximately_equal
from math import pi
from matrix.matrix import Matrix

def test_camera_creation():
    c = Camera(160, 120, pi / 2)
    assert is_approximately_equal(c.hsize, 160)
    assert is_approximately_equal(c.vsize, 120)
    assert is_approximately_equal(c.field_of_view, pi / 2)
    assert c.transform == Matrix.generate_identity_matrix(4)

def test_pixel_size_horizontal_canvas():
    c = Camera(200, 125, pi / 2)
    assert is_approximately_equal(c.pixel_size, 0.01)

def test_pixel_size_vertical_canvas():
    c = Camera(125, 200, pi / 2)
    assert is_approximately_equal(c.pixel_size, 0.01)
