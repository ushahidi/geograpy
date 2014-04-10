from geograpy.extraction import Extractor

def test():
    e = Extractor(url='http://www.bbc.com/news/world-europe-26919928')
    e.find_entities()

    assert len(e.places) > 0
    assert 'Russia' in e.places
    assert 'Kiev' in e.places
