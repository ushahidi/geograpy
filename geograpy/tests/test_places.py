from geograpy.places import PlaceContext

def test():
    pc = PlaceContext(['Ngong', 'Nairobi', 'Kenya'])
    pc.set_countries()
    pc.set_regions()
    pc.set_cities()
    pc.set_other()

    assert len(pc.countries) == 1
    assert len(pc.cities) == 1
    assert len(pc.other) == 1
    assert 'Ngong' in pc.other