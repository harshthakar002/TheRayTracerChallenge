from figures.group import Group
from matrix.matrix import Matrix

def test_create_new_group():
    g = Group()
    assert g.transform == Matrix.generate_identity_matrix(4)
    assert g.is_empty()