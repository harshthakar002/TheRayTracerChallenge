from features.tuple import tuple
from features.equality import isApproximatelyEqual


def test_tuple_point():
    a = tuple(4.3, -4.2, 3.1, 1.0)
    assert isApproximatelyEqual(a.x, 4.3)
    assert isApproximatelyEqual(a.y, -4.2)
    assert isApproximatelyEqual(a.z, 3.1)
    assert isApproximatelyEqual(a.w, 1.0)
    assert a.isPoint()
    assert not a.isVector()


def test_tuple_vector():
    a = tuple(4.3, -4.2, 3.1, 0.0)
    assert isApproximatelyEqual(a.x, 4.3)
    assert isApproximatelyEqual(a.y, -4.2)
    assert isApproximatelyEqual(a.z, 3.1)
    assert isApproximatelyEqual(a.w, 0.0)
    assert not a.isPoint()
    assert a.isVector()


def test_equals():
    a = tuple(1.0, 2.0, -3.0, 1.0)
    assert a.equals(tuple(1.0, 2.0, -3.0, 1.0))


def test_addition():
    a1 = tuple(3, -2, 5, 1)
    a2 = tuple(-2, 3, 1, 0)
    a3 = a1 + a2
    assert a3.equals(tuple(1, 1, 6, 1))
