from features.point import Point
from wavefront.parsed_obj import ParsedObj

def test_parsed_obj_creation():
    parsed_obj = ParsedObj()
    assert parsed_obj.processed == 0
    assert parsed_obj.ignored == 0

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
    assert parsed_obj.processed == 2
    assert parsed_obj.vertices[1] == Point(1, 2, 3)
    assert parsed_obj.vertices[2] == Point(2, 3, 4)