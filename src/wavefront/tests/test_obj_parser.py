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