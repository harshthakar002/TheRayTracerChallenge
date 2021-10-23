from features.tuple import tuple
from features.equality import is_approximately_equal


def test_tuple_point():
    a = tuple(4.3, -4.2, 3.1, 1.0)
    assert is_approximately_equal(a.x, 4.3)
    assert is_approximately_equal(a.y, -4.2)
    assert is_approximately_equal(a.z, 3.1)
    assert is_approximately_equal(a.w, 1.0)
    assert a.is_point()
    assert not a.is_vector()


def test_tuple_vector():
    a = tuple(4.3, -4.2, 3.1, 0.0)
    assert is_approximately_equal(a.x, 4.3)
    assert is_approximately_equal(a.y, -4.2)
    assert is_approximately_equal(a.z, 3.1)
    assert is_approximately_equal(a.w, 0.0)
    assert not a.is_point()
    assert a.is_vector()


def test_equals():
    a = tuple(1.0, 2.0, -3.0, 1.0)
    assert a == tuple(1.0, 2.0, -3.0, 1.0)

def test_not_equals():
    a = tuple(1.0, 2.0, -3.0, 1.0)
    assert a != tuple(1.0, 3.0, -3.0, 1.0)


def test_addition():
    a1 = tuple(3, -2, 5, 1)
    a2 = tuple(-2, 3, 1, 0)
    a3 = a1 + a2
    assert a3 == tuple(1, 1, 6, 1)

def test_negate_tuple():
    a = tuple(1, -2, 3, -4)
    b = a.negate()
    assert b == tuple(-1, 2, -3, 4)


def test_multiply_tuple_by_scalar():
    a = tuple(1, -2, 3, -4)
    b = a * 3.5
    assert b == tuple(3.5, -7, 10.5, -14)

def test_multiply_tuple_by_fraction():
    a = tuple(1, -2, 3, -4)
    b = a * 0.5
    assert b == tuple(0.5, -1, 1.5, -2)

def test_divide_tuple_by_scalar():
    a = tuple(1, -2, 3, -4)
    b = a / 2
    assert b == tuple(0.5, -1, 1.5, -2)