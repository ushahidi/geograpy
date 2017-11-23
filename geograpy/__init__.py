from .extraction import Extractor
from .places import PlaceContext


def get_place_context(url=None, text=None):
    e = Extractor(url=url, text=text)
    e.find_entities()

    pc = PlaceContext(e.places)
    pc.set_countries()
    pc.set_regions()
    pc.set_cities()
    pc.set_other()

    return pc
