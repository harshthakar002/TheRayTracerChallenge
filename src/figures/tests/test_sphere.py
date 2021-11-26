from features.vector import Vector
from figures.ray import Ray
from figures.sphere import Sphere, GlassSphere
from features.point import Point
from features.vector import Vector
from features.equality import is_approximately_equal
from matrix.matrix import Matrix
from physical.material import Material
from transformations.figure_transformer import FigureTransformer
from figures.intersection import Intersection
from math import sqrt, pi
from transformations.transformer import Transformer

def test_ray_intersects_sphere_at_two_points():
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], 4.0)
    assert is_approximately_equal(xs[1], 6.0)

def test_ray_intersects_sphere_at_tangent():
    r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], 5.0)
    assert is_approximately_equal(xs[1], 5.0)

def test_ray_misses_sphere():
    r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 0

def test_ray_originates_in_sphere():
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], -1)
    assert is_approximately_equal(xs[1], 1)

def test_sphere_is_behind_ray():
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    xs = s.ray_intersection_distance(r)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0], -6)
    assert is_approximately_equal(xs[1], -4)

def test_spehere_default_transformation():
    s = Sphere()
    assert s.transform == Matrix.generate_identity_matrix(4)
    assert s.ray_transform == Matrix.generate_identity_matrix(4)

def test_changing_sphere_transformation():
    s = Sphere()
    transform = Transformer.translation(2, 3, 4)
    s.set_transform(transform)
    assert s.transform == transform
    assert s.ray_transform.multiply_matrices(transform) == Matrix.generate_identity_matrix(4)

def test_scaled_sphere_ray_intersection():
    s = Sphere()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s.scaling(2, 2, 2)
    xs = Intersection.find_intersections_of_ray_and_figure(r, s)
    assert len(xs) == 2
    assert is_approximately_equal(xs[0].t, 3)
    assert is_approximately_equal(xs[1].t, 7)

def test_translated_sphere_ray_intersection():
    s = Sphere()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s.translation(5, 0, 0)
    xs = Intersection.find_intersections_of_ray_and_figure(r, s)
    assert len(xs) == 0

def test_normal_on_x_axis():
    s = Sphere()
    n = s.normal_at(Point(1, 0, 0))
    assert n == Vector(1, 0, 0)

def test_normal_on_y_axis():
    s = Sphere()
    n = s.normal_at(Point(0, 1, 0))
    assert n == Vector(0, 1, 0)

def test_normal_on_z_axis():
    s = Sphere()
    n = s.normal_at(Point(0, 0, 1))
    assert n == Vector(0, 0, 1)

def test_normal_at_a_non_axial_point():
    s = Sphere()
    n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
    assert n == Vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3)

def test_normal_is_a_normalized_vector():
    s = Sphere()
    n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
    assert n == n.normalize()

def test_normal_on_translated_sphere():
    s = Sphere()
    s.translation(0, 1, 0)
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    assert n == Vector(0, 0.70711, -0.70711)

def test_normal_on_transformed_sphere():
    s = Sphere()
    s.scaling(1, 0.5, 1).rotation_z(pi / 5)
    n = s.normal_at(Point(0, sqrt(2) / 2, -sqrt(2) / 2))
    assert n == Vector(0, 0.97014, -0.24254)

def test_sphere_has_default_material():
    s = Sphere()
    m = s.material
    assert m == Material()

def test_sphere_may_be_assigned_material():
    s = Sphere()
    m = Material()
    m.ambient = 1
    s.material = m
    assert s.material == m

def test_glass_sphere():
    s = GlassSphere()
    assert s.transform == Matrix.generate_identity_matrix(4)
    assert s.ray_transform == Matrix.generate_identity_matrix(4)
    assert is_approximately_equal(s.material.transparency, 1.0)
    assert is_approximately_equal(s.material.refractive_index, 1.5)