from __future__ import annotations
from features.point import Point
from features.vector import Vector
from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from physical.camera import Camera

class Ray():

    def __init__(self, origin: Point, direction: Vector) -> None:
        self.origin = origin
        self.direction = direction

    def position(self, time: float) -> Point:
        return self.origin + (self.direction * time)

    def get_transformed_ray(self, origin_transformation: Matrix, direction_transformation: Matrix) -> Ray:
        new_origin = origin_transformation.multiply_matrix_and_tuple(self.origin)
        new_direction = direction_transformation.multiply_matrix_and_tuple(self.direction)
        return Ray(new_origin, new_direction)

    @staticmethod
    def ray_for_pixel(camera: Camera, px: float, py: float) -> Ray:
        x_offset = (px + 0.5) * camera.pixel_size
        y_offset = (py + 0.5) * camera.pixel_size

        world_x = camera.half_width - x_offset
        world_y = camera.half_height - y_offset

        inverse_transform = MatrixInverter.invert(camera.transform)

        pixel = inverse_transform.multiply_matrix_and_tuple(Point(world_x, world_y, -1))
        origin = inverse_transform.multiply_matrix_and_tuple(Point(0, 0, 0))
        direction = Vector.fromtuple(pixel - origin).normalize()
        
        return Ray(origin, direction)