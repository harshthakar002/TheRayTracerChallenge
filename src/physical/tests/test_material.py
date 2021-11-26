from features.color import Color
from physical.material import Material
from features.equality import is_approximately_equal

def test_default_material():
    m = Material()
    assert m.color == Color(1, 1, 1)
    assert is_approximately_equal(m.ambient, 0.1)
    assert is_approximately_equal(m.diffuse, 0.9)
    assert is_approximately_equal(m.specular, 0.9)
    assert is_approximately_equal(m.shininess, 200.0)
    assert is_approximately_equal(m.reflective, 0.0)
    assert is_approximately_equal(m.transparency, 0.0)
    assert is_approximately_equal(m.refractive_index, 1.0)
    assert m.pattern == None