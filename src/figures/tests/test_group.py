from figures.group import Group
from figures.shape import Shape
from matrix.matrix import Matrix

def test_create_new_group():
    g = Group()
    assert g.transform == Matrix.generate_identity_matrix(4)
    assert g.is_empty()

def test_add_child_to_a_group():
    g = Group()
    s = Shape()
    g.add_child(s)
    assert not g.is_empty()
    assert g.contains(s)
    assert s.parent == g