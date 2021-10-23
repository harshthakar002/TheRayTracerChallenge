from matrix.matrix import Matrix
from matrix.matrix_inverter import MatrixInverter
from features.equality import is_approximately_equal

def test_determinant_for_2_x_2_matrix():
    m = Matrix.initialize_from_values([[1, 5], [-3, 2]])
    assert is_approximately_equal(MatrixInverter.calculate_determinant_for_2_x_2_matrix(m), 17)

def test_sub_matrix_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
    sub_matrix = MatrixInverter.create_sub_matrix(m, 0, 2)
    excepted_result = m.initialize_from_values([[-3, 2], [0, 6]])
    assert sub_matrix.row_count == 2
    assert sub_matrix.column_count == 2
    assert sub_matrix == excepted_result

def test_sub_matrix_of_4_x_4_matrix():
    m = Matrix.initialize_from_values([[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])
    expected_result = Matrix.initialize_from_values([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])
    sub_matrix = MatrixInverter.create_sub_matrix(m, 2, 1)
    assert sub_matrix.row_count == 3
    assert sub_matrix.column_count == 3
    assert sub_matrix == expected_result

def test_minor_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    assert is_approximately_equal(MatrixInverter.calculate_minor_for_3_x_3_matrix(m, 1, 0), 25)

def test_cofactor_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    assert is_approximately_equal(MatrixInverter.calculate_minor_for_3_x_3_matrix(m, 0, 0), -12)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor_for_3_x_3_matrix(m, 0, 0), -12)
    assert is_approximately_equal(MatrixInverter.calculate_minor_for_3_x_3_matrix(m, 1, 0), 25)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor_for_3_x_3_matrix(m, 1, 0), -25)

def test_determinant_of_3_x_3_matrix():
    m = Matrix.initialize_from_values([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 0), 56)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 1), 12)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 2), -46)
    assert is_approximately_equal(MatrixInverter.calculate_determinant(m), -196)

def test_determinant_of_4_x_4_matrix():
    m = Matrix.initialize_from_values([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 0), 690)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 1), 447)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 2), 210)
    assert is_approximately_equal(MatrixInverter.calculate_cofactor(m, 0, 3), 51)
    assert is_approximately_equal(MatrixInverter.calculate_determinant(m), -4071)