from __future__ import annotations
from matrix.matrix import Matrix
from transformations.transformer import Transformer

class Transformable():

    def __init__(self) -> None:
        raise NotImplementedError('Cannot initialise transformable')

    
    def translation(self, x: float, y: float, z: float) -> Transformable:
        self.set_transform(Transformer.translation(x, y, z))
        return self
    
    def scaling(self, x: float, y: float, z: float) -> Transformable:
        self.set_transform(Transformer.scaling(x, y, z))
        return self

    def rotation_x(self, angle: float) -> Transformable:
        self.set_transform(Transformer.rotation_x(angle))
        return self
    
    def rotation_y(self, angle: float) -> Transformable:
        self.set_transform(Transformer.rotation_y(angle))
        return self
    
    def rotation_z(self, angle: float) -> Transformable:
        self.set_transform(Transformer.rotation_z(angle))
        return self

    def shearing(self, xy: float, xz: float, yx: float, yz: float, zx: float, zy: float) -> Transformable:
        self.set_transform(Transformer.shearing(xy, xz, yx, yz, zx, zy))
        return self

    def set_transform(transform: Matrix) -> Transformable:
        raise NotImplementedError('Not implemented')