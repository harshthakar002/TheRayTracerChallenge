from figures.csg import CSG, CSGOperation
from figures.cube import Cube
from figures.sphere import Sphere

def test_csg_construction():
    s1 = Sphere()
    s2 = Cube()
    c = CSG(CSGOperation.UNION, s1, s2)
    assert c.operation == CSGOperation.UNION
    assert c.left == s1
    assert c.right == s2
    assert s1.parent == c
    assert s2.parent == c