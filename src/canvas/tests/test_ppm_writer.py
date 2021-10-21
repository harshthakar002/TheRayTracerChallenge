from canvas.canvas import canvas
from canvas.ppm_writer import ppm_writer
from features.color import color

def test_ppm_header():
    c = canvas(5, 3)
    ppm = ppm_writer.write_ppm_from_canvas(c)
    assert ppm[0] == 'P3'
    assert ppm[1] == '5 3'
    assert ppm[2] == '255'

def test_ppm_pixel_data():
    c = canvas(5, 3)
    c1, c2, c3 = color(1.5, 0, 0), color(0, 0.5, 0), color(-0.5, 0, 1)
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = ppm_writer.write_ppm_from_canvas(c)
    #assert ppm == ['P3', '5 3', '255']
    assert ppm[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    assert ppm[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
    assert ppm[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"
