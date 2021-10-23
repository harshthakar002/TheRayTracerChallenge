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