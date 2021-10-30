from physical.world import World

def test_world_creation():
    w = World()
    assert len(w.light_sources) == 0
    assert len(w.objects) == 0