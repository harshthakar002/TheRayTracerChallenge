from wavefront.obj_parser import ObjParser

def test_obj_parser_creation():
    obj_parser = ObjParser('test.obj')
    assert obj_parser.filename == 'test.obj'

def test_obj_parser_gibberish():
    obj_parser = ObjParser('src\\wavefront\\tests\\test_files\\gibberish.obj')
    parsed_obj = obj_parser.parse()
    assert parsed_obj.ignored == 5