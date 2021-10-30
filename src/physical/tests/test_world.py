from physical.world import World

def test_world_creation():
    w = World()
    assert w.light == None
    assert len(w.objects) == 0