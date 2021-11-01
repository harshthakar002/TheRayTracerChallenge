from typing import List, Union
from features.equality import is_approximately_equal
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
        
    @staticmethod
    def invert(m: Matrix) -> Union[Matrix, None]:
        if m.row_count == 4 and m.column_count == 4:
            return MatrixInverter.fast_invert_4_x_4_matrix(m)
        determinant = MatrixInverter.calculate_determinant(m)
        if is_approximately_equal(determinant, 0):
            return None
        cofactor_m = MatrixInverter.generate_cofactor_matrix(m)
        transpose_cofactor = cofactor_m.transposed_matrix()
        transpose_cofactor.divide_by_scalar(determinant)
        return transpose_cofactor
    
    @staticmethod
    def generate_cofactor_matrix(m: Matrix):
        cofactor_matrix = Matrix(m.row_count, m.column_count)
        for i in range(cofactor_matrix.row_count):
            for j in range(cofactor_matrix.column_count):
                cofactor_matrix.set(i, j, MatrixInverter.calculate_cofactor(m, i, j))
        return cofactor_matrix
    
    @staticmethod
    def fast_invert_4_x_4_matrix(matrix: Matrix) -> Matrix:
        inv: List[float] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        m = matrix.data[0] + matrix.data[1] + matrix.data[2] + matrix.data[3]
        inv[0] = (m[5]  * m[10] * m[15] - 
             m[5]  * m[11] * m[14] - 
             m[9]  * m[6]  * m[15] + 
             m[9]  * m[7]  * m[14] +
             m[13] * m[6]  * m[11] - 
             m[13] * m[7]  * m[10])

        inv[4] = (-m[4]  * m[10] * m[15] + 
              m[4]  * m[11] * m[14] + 
              m[8]  * m[6]  * m[15] - 
              m[8]  * m[7]  * m[14] - 
              m[12] * m[6]  * m[11] + 
              m[12] * m[7]  * m[10])

        inv[8] = (m[4]  * m[9] * m[15] - 
             m[4]  * m[11] * m[13] - 
             m[8]  * m[5] * m[15] + 
             m[8]  * m[7] * m[13] + 
             m[12] * m[5] * m[11] - 
             m[12] * m[7] * m[9])

        inv[12] = (-m[4]  * m[9] * m[14] + 
               m[4]  * m[10] * m[13] +
               m[8]  * m[5] * m[14] - 
               m[8]  * m[6] * m[13] - 
               m[12] * m[5] * m[10] + 
               m[12] * m[6] * m[9])

        inv[1] = (-m[1]  * m[10] * m[15] + 
              m[1]  * m[11] * m[14] + 
              m[9]  * m[2] * m[15] - 
              m[9]  * m[3] * m[14] - 
              m[13] * m[2] * m[11] + 
              m[13] * m[3] * m[10])

        inv[5] = (m[0]  * m[10] * m[15] - 
             m[0]  * m[11] * m[14] - 
             m[8]  * m[2] * m[15] + 
             m[8]  * m[3] * m[14] + 
             m[12] * m[2] * m[11] - 
             m[12] * m[3] * m[10])

        inv[9] = (-m[0]  * m[9] * m[15] + 
              m[0]  * m[11] * m[13] + 
              m[8]  * m[1] * m[15] - 
              m[8]  * m[3] * m[13] - 
              m[12] * m[1] * m[11] + 
              m[12] * m[3] * m[9])

        inv[13] = (m[0]  * m[9] * m[14] - 
              m[0]  * m[10] * m[13] - 
              m[8]  * m[1] * m[14] + 
              m[8]  * m[2] * m[13] + 
              m[12] * m[1] * m[10] - 
              m[12] * m[2] * m[9])

        inv[2] = (m[1]  * m[6] * m[15] - 
             m[1]  * m[7] * m[14] - 
             m[5]  * m[2] * m[15] + 
             m[5]  * m[3] * m[14] + 
             m[13] * m[2] * m[7] - 
             m[13] * m[3] * m[6])

        inv[6] = (-m[0]  * m[6] * m[15] + 
              m[0]  * m[7] * m[14] + 
              m[4]  * m[2] * m[15] - 
              m[4]  * m[3] * m[14] - 
              m[12] * m[2] * m[7] + 
              m[12] * m[3] * m[6])

        inv[10] = (m[0]  * m[5] * m[15] - 
              m[0]  * m[7] * m[13] - 
              m[4]  * m[1] * m[15] + 
              m[4]  * m[3] * m[13] + 
              m[12] * m[1] * m[7] - 
              m[12] * m[3] * m[5])

        inv[14] = (-m[0]  * m[5] * m[14] + 
               m[0]  * m[6] * m[13] + 
               m[4]  * m[1] * m[14] - 
               m[4]  * m[2] * m[13] - 
               m[12] * m[1] * m[6] + 
               m[12] * m[2] * m[5])

        inv[3] = (-m[1] * m[6] * m[11] + 
              m[1] * m[7] * m[10] + 
              m[5] * m[2] * m[11] - 
              m[5] * m[3] * m[10] - 
              m[9] * m[2] * m[7] + 
              m[9] * m[3] * m[6])

        inv[7] = (m[0] * m[6] * m[11] - 
             m[0] * m[7] * m[10] - 
             m[4] * m[2] * m[11] + 
             m[4] * m[3] * m[10] + 
             m[8] * m[2] * m[7] - 
             m[8] * m[3] * m[6])

        inv[11] = (-m[0] * m[5] * m[11] + 
               m[0] * m[7] * m[9] + 
               m[4] * m[1] * m[11] - 
               m[4] * m[3] * m[9] - 
               m[8] * m[1] * m[7] + 
               m[8] * m[3] * m[5])

        inv[15] = (m[0] * m[5] * m[10] - 
              m[0] * m[6] * m[9] - 
              m[4] * m[1] * m[10] + 
              m[4] * m[2] * m[9] + 
              m[8] * m[1] * m[6] - 
              m[8] * m[2] * m[5])
        
        det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12]

        if det == 0:
            return None

        inverted_values: List[List[float]] = [[], [], [], []]

        for i in range(len(inv)):
            inverted_values[int(i / 4)].append(inv[i] / det)

        inverted_matrix = Matrix.initialize_from_values(inverted_values)
        return inverted_matrix