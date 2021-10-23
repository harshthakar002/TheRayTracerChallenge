from matrix.matrix import Matrix

class Transformer():

    @staticmethod
    def translation(x: int, y: int, z: int) -> Matrix:
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