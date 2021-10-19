from canvas.canvas import canvas
from features.color import color

def test_canvas_creation():
    c = canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for row in c.pixels:
        for pixel in row:
            assert pixel == color(0, 0, 0)