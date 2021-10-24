from typing import Tuple as Group
from matrix.matrix import Matrix
from transformations.transformer import Transformer

class FigureTransformer():

    @staticmethod
    def translation(x: float, y: float, z: float) -> Group[Matrix, Matrix]:
        m = Transformer.translation(x, y, z)
        return m, Matrix.generate_identity_matrix(4)
    
    @staticmethod
    def scaling(x: float, y: float, z: float) -> Group[Matrix, Matrix]:
        m = Transformer.scaling(x, y, z)
        return m, m
    
    @staticmethod
    def rotation_x(angle: float) -> Group[Matrix, Matrix]:
        m = Transformer.rotation_x(angle)
        return m, m
    
    @staticmethod
    def rotation_y(angle: float) -> Group[Matrix, Matrix]:
        m = Transformer.rotation_y(angle)
        return m, m
    
    @staticmethod
    def rotation_z(angle: float) -> Group[Matrix, Matrix]:
        m = Transformer.rotation_z(angle)
        return m, m

    @staticmethod
    def shearing(xy: float, xz: float, yx: float, yz: float, zx: float, zy: float) -> Group[Matrix, Matrix]:
        m = Transformer.shearing(xy, xz, yx, yz, zx, zy)
        return m, m