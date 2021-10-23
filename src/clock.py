from transformations.transformer import Transformer
from canvas.canvas import Canvas
from canvas.ppm_writer import PPMWriter
from features.color import Color
from features.point import Point
from math import pi

start_p = Point(0, 0, 0)
c = Canvas(500, 500)
translation = Transformer.translation(200, 0, 0)
tick = Transformer.rotation_z(pi / 6)
p = translation.multiply_matrix_and_tuple(start_p)
for i in range(12):
    c.write_pixel(round(p.x) + 250, round(p.y) + 250, Color(1, 1, 1))
    p = tick.multiply_matrix_and_tuple(p)

ppm = PPMWriter.write_ppm_from_canvas(c)
with open('out/clock.ppm', 'w') as f:
    f.write('\n'.join(ppm))
