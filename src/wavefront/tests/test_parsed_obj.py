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