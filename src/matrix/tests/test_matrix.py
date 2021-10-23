from matrix.matrix import Matrix
from features.equality import is_approximately_equal

def test_matrix_creation():
    mat = Matrix(4, 4)
    assert mat.row_count == 4
    assert mat.column_count == 4
    assert mat.data == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_matrix_construction():
    mat = Matrix.initialize_from_values([[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12],[13.5, 14.5, 15.5, 16.5]])
    is_approximately_equal(mat.get(0, 0), 1)
    is_approximately_equal(mat.get(0, 1), 2)
    is_approximately_equal(mat.get(0, 2), 3)
    is_approximately_equal(mat.get(0, 3), 4)
    is_approximately_equal(mat.get(1, 0), 5.5)
    is_approximately_equal(mat.get(1, 1), 6.5)
    is_approximately_equal(mat.get(1, 2), 7.5)
    is_approximately_equal(mat.get(1, 3), 8.5)
    is_approximately_equal(mat.get(2, 0), 9)
    is_approximately_equal(mat.get(2, 1), 10)
    is_approximately_equal(mat.get(2, 2), 11)
    is_approximately_equal(mat.get(2, 3), 12)
    is_approximately_equal(mat.get(3, 0), 13.5)
    is_approximately_equal(mat.get(3, 1), 14.5)
    is_approximately_equal(mat.get(3, 2), 15.5)
    is_approximately_equal(mat.get(3, 3), 16.5)

def test_2_x_2_matrix_construction():
    mat = Matrix.initialize_from_values([[-3, 5], [1, -2]])
    assert is_approximately_equal(mat.get(0, 0), -3)
    assert is_approximately_equal(mat.get(0, 1), 5)
    assert is_approximately_equal(mat.get(1, 0), 1)
    assert is_approximately_equal(mat.get(1, 1), -2)

def test_3_x_3_matrix_construction():
    mat = Matrix.initialize_from_values([[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
    assert is_approximately_equal(mat.get(0, 0), -3)
    assert is_approximately_equal(mat.get(1, 1), -2)
    assert is_approximately_equal(mat.get(2, 2), 1)

def test_matrix_equality():
    a = Matrix.initialize_from_values([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    b = Matrix.initialize_from_values([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    assert a == b

def test_matrix_inequality():
    a = Matrix.initialize_from_values([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    b = Matrix.initialize_from_values([[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
    assert a != b

def test_identity_matrix_generation():
    identity_matrix = Matrix.generate_identity_matrix(3)
    m = Matrix.initialize_from_values([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert identity_matrix == m

def test_matrix_transpose():
    m = Matrix.initialize_from_values([[0, 9, 3, 0], [9, 8, 0, 8], [1, 8, 5, 3], [0, 0, 5, 8]])
    transposed_m = Matrix.initialize_from_values([[0, 9, 1, 0], [9, 8, 8, 0], [3, 0, 5, 5], [0, 8, 3, 8]])
    assert m.transposed_matrix() == transposed_m

def test_identity_matrix_transpose():
    identity_matrix = Matrix.generate_identity_matrix(3)
    assert identity_matrix.transposed_matrix() == identity_matrix

def test_multiply_with_scalar():
    m = Matrix.initialize_from_values([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m.multiply_with_scalar(2)
    expected_result = Matrix.initialize_from_values([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    assert m == expected_result

def test_divide_by_scalar():
    m = Matrix.initialize_from_values([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    m.divide_by_scalar(2)
    expected_result = Matrix.initialize_from_values([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert m == expected_result