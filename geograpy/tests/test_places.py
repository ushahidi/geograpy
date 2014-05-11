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

    assert pc.cities_for_name('Nairobi')[0][4] == 'Kenya'
    assert pc.regions_for_name('Ohio')[0][4] == 'United States'

    pc = PlaceContext(['Aleppo', 'Syria'])
    pc.set_countries()
    pc.set_regions()
    pc.set_cities()
    pc.set_other()

    assert 'Aleppo' in pc.cities