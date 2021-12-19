from features.point import Point
from features.vector import Vector
from figures.group import Group
from figures.intersection import Intersection
from figures.ray import Ray
from figures.shape import Shape
from figures.sphere import Sphere
from matrix.matrix import Matrix
from math import pi, sqrt

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

def test_intersecting_ray_with_empty_group():
    g = Group()
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, g)
    assert len(xs) == 0

def test_intersecting_ray_with_non_empty_group():
    g = Group()
    s1 = Sphere()
    s2 = Sphere()
    s2.translation(0, 0, -3)
    s3 = Sphere()
    s3.translation(5, 0, 0)
    g.add_child(s1)
    g.add_child(s2)
    g.add_child(s3)
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, g)
    assert len(xs) == 4
    assert xs[0].object == s2
    assert xs[1].object == s2
    assert xs[2].object == s1
    assert xs[3].object == s1

def test_intersecting_a_transformed_group():
    g = Group()
    g.scaling(2, 2, 2)
    s = Sphere()
    s.translation(5, 0, 0)
    g.add_child(s)
    r = Ray(Point(10, 0, -10), Vector(0, 0, 1))
    xs = Intersection.find_intersections_of_ray_and_figure(r, g)
    assert len(xs) == 2

def test_convert_a_point_from_world_to_object_space():
    g1 = Group()
    g1.rotation_y(pi / 2)
    g2 = Group()
    g2.scaling(2, 2, 2)
    g1.add_child(g2)
    s = Sphere()
    s.translation(5, 0 ,0)
    g2.add_child(s)
    p = s.world_to_object(Point(-2, 0, -10))
    assert p == Point(0, 0, -1)

def test_convert_normal_from_object_space_to_world_space():
    g1 = Group()
    g1.rotation_y(pi / 2)
    g2 = Group()
    g2.scaling(1, 2, 3)
    g1.add_child(g2)
    s = Sphere()
    s.translation(5, 0, 0)
    g2.add_child(s)
    n = s.normal_to_world(Vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
    assert n == Vector(0.28571, 0.42857, -0.85714)