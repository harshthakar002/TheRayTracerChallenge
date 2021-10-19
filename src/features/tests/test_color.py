from features.color import color
from features.equality import isApproximatelyEqual

def test_color_creation():
    c = color(-0.5, 0.4, 1.7)
    assert isApproximatelyEqual(c.red, -0.5)
    assert isApproximatelyEqual(c.green, 0.4)
    assert isApproximatelyEqual(c.blue, 1.7)
    c.x = 0.1
    assert isApproximatelyEqual(c.red, 0.1)

def test_color_addition():
    c1 = color(0.9, 0.6, 0.75)
    c2 = color(0.7, 0.1, 0.25)
    c3 = c1 + c2
    assert c3 == color(1.6, 0.7, 1.0)

def test_color_subtraction():
    c1 = color(0.9, 0.6, 0.75)
    c2 = color(0.7, 0.1, 0.25)
    c3 = c1 - c2
    assert c3 == color(0.2, 0.5, 0.5)

def test_color_scalar_multiplication():
    c1 = color(0.2, 0.3, 0.4)
    c2 = c1 * 2
    assert c2 == color(0.4, 0.6, 0.8)

def test_color_scalar_division():
    c1 = color(0.4, 0.6, 0.8)
    c2 = c1 / 2
    assert c2 == color(0.2, 0.3, 0.4)

def test_color_multiplication():
    c1 = color(1, 0.2, 0.4)
    c2 = color(0.9, 1, 0.1)
    c3 = c1.multiply(c2)
    assert c3 == color(0.9, 0.2, 0.04)