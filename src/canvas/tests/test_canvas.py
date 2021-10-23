from canvas.canvas import canvas
from features.color import color

def test_canvas_creation():
    c = canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for row in c.pixels:
        for pixel in row:
            assert pixel == color(0, 0, 0)

def test_canvas_write_pixel():
    c = canvas(10, 20)
    red = color(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red
    assert c.pixel_at(0, 0) == color(0, 0, 0)

def test_canvas_vertically_flip():
    c = canvas(2, 2)
    c.write_pixel(0, 0, color(1, 0, 0))
    assert c.pixel_at(0, 0) == color(1, 0, 0)
    assert c.pixel_at(0, 1) == color(0, 0, 0)
    c.vertically_flip()
    assert c.pixel_at(0, 0) == color(0, 0, 0)
    assert c.pixel_at(0, 1) == color(1, 0, 0)