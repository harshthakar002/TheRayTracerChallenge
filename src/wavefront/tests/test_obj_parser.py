from wavefront.obj_parser import ObjParser

def test_obj_parser_creation():
    obj_parser = ObjParser('test.obj')
    assert obj_parser.filename == 'test.obj'