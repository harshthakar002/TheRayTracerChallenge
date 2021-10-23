from matrix.matrix import Matrix
from math import cos, sin

class Transformer():

    @staticmethod
    def translation(x: float, y: float, z: float) -> Matrix:
        translation_matrix = Matrix.generate_identity_matrix(4)
        translation_matrix.set(0, 3, x)
        translation_matrix.set(1, 3, y)
        translation_matrix.set(2, 3, z)
        return translation_matrix
    
    @staticmethod
    def scaling(x: float, y: float, z: float) -> Matrix:
        scaling_matrix = Matrix.generate_identity_matrix(4)
        scaling_matrix.set(0, 0, x)
        scaling_matrix.set(1, 1, y)
        scaling_matrix.set(2, 2, z)
        return scaling_matrix

    @staticmethod
    def rotation_x(angle: float) -> Matrix:
        rotation_matrix = Matrix.generate_identity_matrix(4)
        rotation_matrix.set(1, 1, cos(angle))
        rotation_matrix.set(1, 2, -sin(angle))
        rotation_matrix.set(2, 1, sin(angle))
        rotation_matrix.set(2, 2, cos(angle))
        return rotation_matrix
    
    @staticmethod
    def rotation_y(angle: float) -> Matrix:
        rotation_matrix = Matrix.generate_identity_matrix(4)
        rotation_matrix.set(0, 0, cos(angle))
        rotation_matrix.set(2, 0, -sin(angle))
        rotation_matrix.set(0, 2, sin(angle))
        rotation_matrix.set(2, 2, cos(angle))
        return rotation_matrix
    
    @staticmethod
    def rotation_z(angle: float) -> Matrix:
        rotation_matrix = Matrix.generate_identity_matrix(4)
        rotation_matrix.set(0, 0, cos(angle))
        rotation_matrix.set(0, 1, -sin(angle))
        rotation_matrix.set(1, 0, sin(angle))
        rotation_matrix.set(1, 1, cos(angle))
        return rotation_matrix
    