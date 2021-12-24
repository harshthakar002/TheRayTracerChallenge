from features.point import Point
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
    assert len(parsed_obj.default_group.shapes) == 2
    assert parsed_obj.default_group.shapes[0].p1 == parsed_obj.vertices[1]
    assert parsed_obj.default_group.shapes[0].p2 == parsed_obj.vertices[2]
    assert parsed_obj.default_group.shapes[0].p3 == parsed_obj.vertices[3]
    assert parsed_obj.default_group.shapes[1].p1 == parsed_obj.vertices[1]
    assert parsed_obj.default_group.shapes[1].p2 == parsed_obj.vertices[3]
    assert parsed_obj.default_group.shapes[1].p3 == parsed_obj.vertices[4]

def test_obj_parser_polygons():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\polygons.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 1
    assert parsed_obj.processed == 8
    assert len(parsed_obj.vertices) == 6
    assert len(parsed_obj.default_group.shapes) == 3
    assert parsed_obj.default_group.shapes[0].p1 == parsed_obj.vertices[1]
    assert parsed_obj.default_group.shapes[0].p2 == parsed_obj.vertices[2]
    assert parsed_obj.default_group.shapes[0].p3 == parsed_obj.vertices[3]
    assert parsed_obj.default_group.shapes[1].p1 == parsed_obj.vertices[1]
    assert parsed_obj.default_group.shapes[1].p2 == parsed_obj.vertices[3]
    assert parsed_obj.default_group.shapes[1].p3 == parsed_obj.vertices[4]
    assert parsed_obj.default_group.shapes[2].p1 == parsed_obj.vertices[1]
    assert parsed_obj.default_group.shapes[2].p2 == parsed_obj.vertices[4]
    assert parsed_obj.default_group.shapes[2].p3 == parsed_obj.vertices[5]