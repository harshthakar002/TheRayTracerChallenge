from features.point import Point
from features.vector import Vector
from wavefront.obj_parser import ObjParser
from wavefront.parsed_obj import ParsedObj

def test_parsed_obj_creation():
    parsed_obj = ParsedObj()
    assert parsed_obj.processed == 0
    assert parsed_obj.ignored == 0
    assert len(parsed_obj.groups) == 1

def test_parsed_obj_ignore():
    parsed_obj = ParsedObj()
    parsed_obj.ignore()
    assert parsed_obj.ignored == 1
    parsed_obj.ignore()
    assert parsed_obj.ignored == 2

def test_parsed_obj_add_vertex():
    parsed_obj = ParsedObj()
    parsed_obj.add_vertex(1, 2, 3)
    parsed_obj.add_vertex(2, 3, 4)
    assert parsed_obj.vertices[1] == Point(1, 2, 3)
    assert parsed_obj.vertices[2] == Point(2, 3, 4)

def test_parsed_obj_add_face():
    parsed_obj = ParsedObj()
    parsed_obj.add_vertex(1, 2, 3)
    parsed_obj.add_vertex(2, 3, 4)
    parsed_obj.add_vertex(3, 4, 5)
    parsed_obj.add_triangle(1, 2, 3)
    assert len(parsed_obj.groups) == 1
    assert len(parsed_obj.groups[0].shapes) == 1
    assert parsed_obj.groups[0].shapes[0].p1 == Point(1, 2, 3)
    assert parsed_obj.groups[0].shapes[0].p2 == Point(2, 3, 4)
    assert parsed_obj.groups[0].shapes[0].p3 == Point(3, 4, 5)

def test_parsed_obj_mark_processed():
    parsed_obj = ParsedObj()
    parsed_obj.mark_processed()
    assert parsed_obj.processed == 1
    parsed_obj.mark_processed()
    assert parsed_obj.processed == 2

def test_parsed_obj_add_group():
    parsed_obj = ParsedObj()
    parsed_obj.add_group('TestGroup')
    assert len(parsed_obj.groups) == 2
    assert parsed_obj.groups[1].name == 'TestGroup'

def test_parsed_obj_as_group():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\triangles.obj')
    parsed_obj = obj_parser.parse()
    g = parsed_obj.asGroup()
    assert g.shapes[0].name == 'FirstGroup'
    assert g.shapes[1].name == 'SecondGroup'

def test_parsed_obj_add_normal():
    parsed_obj = ParsedObj()
    parsed_obj.add_normal(1, 2, 3)
    parsed_obj.add_normal(4, 5, 6)
    assert len(parsed_obj.normals) == 3
    assert parsed_obj.normals[1] == Vector(1, 2, 3)
    assert parsed_obj.normals[2] == Vector(4, 5, 6)