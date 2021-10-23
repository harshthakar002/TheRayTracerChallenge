from features.vector import Vector
from features.point import Point
from features.color import Color
from canvas.canvas import Canvas
from canvas.ppm_writer import PPMWriter


class environment:
    def __init__(self, gravity: Vector, wind: Vector) -> None:
        self.gravity = gravity
        self.wind = wind


class projectile:
    def __init__(self, position: Point, velocity: Vector) -> None:
        self.position = position
        self.velocity = velocity
        self.color = Color(1, 0, 0)


def tick(env: environment, proj: projectile) -> projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)   

p = projectile(Point(0, 1, 0), Vector(1, 1.8, 0).normalize() * 11.25)
e = environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))
c = Canvas(900, 550)

c.write_pixel(round(p.position.x), round(p.position.y), p.color)
while p.position.y > 0:
    p = tick(e, p)
    c.write_pixel(round(p.position.x), round(p.position.y), p.color)

c.vertically_flip()

ppm = PPMWriter.write_ppm_from_canvas(c)

with open('out/imgOut.ppm', 'w') as f:
    f.write('\n'.join(ppm))