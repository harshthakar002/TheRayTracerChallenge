from matrix.matrix import Matrix

class MatrixInverter():

    @staticmethod
    def calculate_determinant_for_2_x_2_matrix(m: Matrix) -> float:
        return (m.get(0, 0) * m.get(1, 1)) - (m.get(0, 1) * m.get(1, 0)) 