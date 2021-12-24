from wavefront.parsed_obj import ParsedObj

def test_parsed_obj_creation():
    parsed_obj = ParsedObj()
    assert parsed_obj.processed == 0
    assert parsed_obj.ignored == 0