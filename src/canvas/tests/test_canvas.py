from canvas.canvas import Canvas
from features.color import Color

def test_canvas_creation():
    c = Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for row in c.pixels:
        for pixel in row:
            assert pixel == Color(0, 0, 0)

def test_canvas_write_pixel():
    c = Canvas(10, 20)
    red = Color(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red
    assert c.pixel_at(0, 0) == Color(0, 0, 0)

def test_canvas_vertically_flip():
    c = Canvas(2, 2)
    c.write_pixel(0, 0, Color(1, 0, 0))
    assert c.pixel_at(0, 0) == Color(1, 0, 0)
    assert c.pixel_at(0, 1) == Color(0, 0, 0)
    c.vertically_flip()
    assert c.pixel_at(0, 0) == Color(0, 0, 0)
    assert c.pixel_at(0, 1) == Color(1, 0, 0)