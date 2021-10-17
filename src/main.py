from features.vector import vector
from features.point import point


class environment:
    def __init__(self, gravity: vector, wind: vector) -> None:
        self.gravity = gravity
        self.wind = wind


class projectile:
    def __init__(self, position: point, velocity: vector) -> None:
        self.position = position
        self.velocity = velocity


def tick(env: environment, proj: projectile) -> projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)


p = projectile(point(0, 1, 0), vector(1, 1, 0).normalize())
e = environment(vector(0, -0.1, 0), vector(-0.01, -0.1, 0))


def print_p(p: projectile) -> None:
    print("Position: (" + str(p.position.x) + ", " + str(p.position.y) + ", " + str(p.position.z) +
          ") Velocity: (" + str(p.velocity.x) + ", " + str(p.velocity.y) + ", " + str(p.velocity.z) + ")")


print_p(p)
count = 0
while p.position.y > 0:
    p = tick(e, p)
    print_p(p)
    count += 1
print(count)