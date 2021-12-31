from features.point import Point
from features.vector import Vector
from wavefront.obj_parser import ObjParser

def test_obj_parser_creation():
    obj_parser = ObjParser('test.obj')
    assert obj_parser.filename == 'test.obj'

def test_obj_parser_gibberish():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\gibberish.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 5

def test_obj_parser_vertices():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\vertices.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 0
    assert parsed_obj.processed == 4
    assert len(parsed_obj.vertices) == 5
    assert parsed_obj.vertices[1] == Point(-1, 1, 0)
    assert parsed_obj.vertices[2] == Point(-1, 0.5, 0)
    assert parsed_obj.vertices[3] == Point(1, 0, 0)
    assert parsed_obj.vertices[4] == Point(1, 1, 0)

def test_obj_parser_faces():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\faces.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 1
    assert parsed_obj.processed == 6
    assert len(parsed_obj.vertices) == 5
    assert len(parsed_obj.groups) == 1
    assert len(parsed_obj.groups[0].shapes) == 2
    assert parsed_obj.groups[0].shapes[0].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[0].shapes[0].p2 == parsed_obj.vertices[2]
    assert parsed_obj.groups[0].shapes[0].p3 == parsed_obj.vertices[3]
    assert parsed_obj.groups[0].shapes[1].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[0].shapes[1].p2 == parsed_obj.vertices[3]
    assert parsed_obj.groups[0].shapes[1].p3 == parsed_obj.vertices[4]

def test_obj_parser_polygons():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\polygons.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 1
    assert parsed_obj.processed == 6
    assert len(parsed_obj.groups) == 1
    assert len(parsed_obj.vertices) == 6
    assert len(parsed_obj.groups[0].shapes) == 3
    assert parsed_obj.groups[0].shapes[0].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[0].shapes[0].p2 == parsed_obj.vertices[2]
    assert parsed_obj.groups[0].shapes[0].p3 == parsed_obj.vertices[3]
    assert parsed_obj.groups[0].shapes[1].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[0].shapes[1].p2 == parsed_obj.vertices[3]
    assert parsed_obj.groups[0].shapes[1].p3 == parsed_obj.vertices[4]
    assert parsed_obj.groups[0].shapes[2].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[0].shapes[2].p2 == parsed_obj.vertices[4]
    assert parsed_obj.groups[0].shapes[2].p3 == parsed_obj.vertices[5]

def test_obj_parser_triangles():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\triangles.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 1
    assert parsed_obj.processed == 8
    assert len(parsed_obj.groups) == 3
    assert len(parsed_obj.vertices) == 5
    assert len(parsed_obj.groups[0].shapes) == 0
    assert parsed_obj.groups[1].name == 'FirstGroup'
    assert len(parsed_obj.groups[1].shapes) == 1
    assert parsed_obj.groups[2].name == 'SecondGroup'
    assert len(parsed_obj.groups[2].shapes) == 1
    assert parsed_obj.groups[1].shapes[0].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[1].shapes[0].p2 == parsed_obj.vertices[2]
    assert parsed_obj.groups[1].shapes[0].p3 == parsed_obj.vertices[3]
    assert parsed_obj.groups[2].shapes[0].p1 == parsed_obj.vertices[1]
    assert parsed_obj.groups[2].shapes[0].p2 == parsed_obj.vertices[3]
    assert parsed_obj.groups[2].shapes[0].p3 == parsed_obj.vertices[4]

def test_obj_parser_normals():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\normals.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 0
    assert parsed_obj.processed == 3
    assert len(parsed_obj.normals) == 4
    assert parsed_obj.normals[1] == Vector(0, 0, 1)
    assert parsed_obj.normals[2] == Vector(0.707, 0, -0.707)
    assert parsed_obj.normals[3] == Vector(1, 2, 3)