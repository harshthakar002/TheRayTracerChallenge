from typing import List
from features.point import Point
from features.vector import Vector
from figures.ray import Ray
from figures.shape import Shape

class Group(Shape):

    def __init__(self) -> None:
        super().__init__()
        self.shapes: List[Shape] = []

    def is_empty(self) -> bool:
        return len(self.shapes) == 0
    
    def contains(self, shape: Shape) -> bool:
        return shape in self.shapes

    def add_child(self, shape: Shape) -> None:
        self.shapes.append(shape)
        shape.parent = self
    
    def local_intersect(self, ray: Ray) -> List[tuple[float, Shape]]:
        transformed_ray = ray.get_transformed_ray(self.ray_transform)
        intersection_distances_and_shapes: List[tuple[float, Shape]] = []
        for shape in self.shapes:
            intersection_distances_and_shapes += shape.local_intersect(transformed_ray)
        return sorted(intersection_distances_and_shapes, key=lambda intersection_distance_and_shape: intersection_distance_and_shape[0])
    
    def normal_at(self, point: Point) -> Vector:
        raise NotImplementedError('This method should not be called for groups')