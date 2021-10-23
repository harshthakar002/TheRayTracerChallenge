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
    
    @staticmethod
    def calculate_minor_for_3_x_3_matrix(m: Matrix, row: int, column: int) -> float:
        sub_matrix = MatrixInverter.create_sub_matrix(m, row, column)
        return MatrixInverter.calculate_determinant_for_2_x_2_matrix(sub_matrix)

    @staticmethod
    def calculate_cofactor(m: Matrix, row: int, column: int) -> float:
        sign = 1
        if row % 2 != column % 2:
            sign = -1
        return sign * MatrixInverter.calculate_minor(m, row, column)
    
    @staticmethod
    def calculate_minor(m: Matrix, row: int, column: int) -> float:
        if m.row_count == 3:
            return MatrixInverter.calculate_minor_for_3_x_3_matrix(m, row, column)
        sub_matrix = MatrixInverter.create_sub_matrix(m, row, column)
        return MatrixInverter.calculate_determinant(sub_matrix)
    
    @staticmethod
    def calculate_determinant(m: Matrix) -> float:
        if m.row_count == 2:
            return MatrixInverter.calculate_determinant_for_2_x_2_matrix(m)
        determinant = 0
        for j in range(m.column_count):
            determinant = determinant + (m.get(0, j) * MatrixInverter.calculate_cofactor(m, 0, j))
        return determinant
        