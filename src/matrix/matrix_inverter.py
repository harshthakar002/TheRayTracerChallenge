from matrix.matrix import Matrix

class MatrixInverter():

    @staticmethod
    def calculate_determinant_for_2_x_2_matrix(m: Matrix) -> float:
        return (m.get(0, 0) * m.get(1, 1)) - (m.get(0, 1) * m.get(1, 0))

    @staticmethod
    def create_sub_matrix(m: Matrix, ignored_row: int, ignored_column: int) -> Matrix:
        sub_matrix_rows = []
        for i in range(m.row_count):
            if i == ignored_row:
                continue
            sub_matrix_rows.append(m.data[i][:ignored_column] + m.data[i][ignored_column + 1:])
        return Matrix.initialize_from_values(sub_matrix_rows)