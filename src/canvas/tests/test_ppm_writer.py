from canvas.canvas import Canvas
from canvas.ppm_writer import PPMWriter
from features.color import color

def test_ppm_header():
    c = Canvas(5, 3)
    ppm = PPMWriter.write_ppm_from_canvas(c)
    assert ppm[0] == 'P3'
    assert ppm[1] == '5 3'
    assert ppm[2] == '255'

def test_ppm_pixel_data():
    c = Canvas(5, 3)
    c1, c2, c3 = color(1.5, 0, 0), color(0, 0.5, 0), color(-0.5, 0, 1)
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = PPMWriter.write_ppm_from_canvas(c)
    assert ppm[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    assert ppm[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
    assert ppm[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"

def test_ppm_line_split():
    c = Canvas(10, 2)
    for i in range(c.width):
        for j in range(c.height):
            c.write_pixel(i, j, color(1, 0.8, 0.6))
    ppm = PPMWriter.write_ppm_from_canvas(c)
    assert ppm[3] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153"
    assert ppm[4] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153"
    assert ppm[5] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153"
    assert ppm[6] == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153"

def test_ppm_new_line_at_end():
    c = Canvas(5, 3)
    ppm = PPMWriter.write_ppm_from_canvas(c)
    assert ppm[len(ppm)-1] == ''
