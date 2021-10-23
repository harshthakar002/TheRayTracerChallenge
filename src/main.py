from features.vector import vector
from features.point import point
from features.color import color
from canvas.canvas import canvas
from canvas.ppm_writer import ppm_writer


class environment:
    def __init__(self, gravity: vector, wind: vector) -> None:
        self.gravity = gravity
        self.wind = wind


class projectile:
    def __init__(self, position: point, velocity: vector) -> None:
        self.position = position
        self.velocity = velocity
        self.color = color(1, 0, 0)


def tick(env: environment, proj: projectile) -> projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)   

p = projectile(point(0, 1, 0), vector(1, 1.8, 0).normalize() * 11.25)
e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))
c = canvas(900, 550)

c.write_pixel(round(p.position.x), round(p.position.y), p.color)
while p.position.y > 0:
    p = tick(e, p)
    c.write_pixel(round(p.position.x), round(p.position.y), p.color)

c.vertically_flip()

ppm = ppm_writer.write_ppm_from_canvas(c)

with open('out/imgOut.ppm', 'w') as f:
    f.write('\n'.join(ppm))