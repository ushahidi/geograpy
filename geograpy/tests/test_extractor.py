# -*- coding: utf-8 -*-

from geograpy.extraction import Extractor

def test():
    e = Extractor(url='http://www.bbc.com/news/world-europe-26919928')
    e.find_entities()

    assert len(e.places) > 0
    assert 'Russia' in e.places
    assert 'Kiev' in e.places
    
    text = """ Perfect just Perfect! It's a perfect storm for Nairobi on a 
    Friday evening! horrible traffic here is your cue to become worse @Ma3Route """

    e2 = Extractor(text=text)
    e2.find_entities()

    assert len(e2.places) > 0
    assert 'Nairobi' in e2.places

    text3 = """ Risks of Cycling in Nairobi:http://www.globalsiteplans.com/environmental-design/engineering-environmental-design/the-risky-affair-of-cycling-in-nairobi-kenya/ ... via @ConstantCap @KideroEvans @county_nairobi @NrbCity_Traffic """
    e3 = Extractor(text=text3)
    e3.find_entities()

    assert len(e3.places) > 0
    assert 'Nairobi' in e3.places

    text4 = """ @DurbanSharks [Africa Renewal]It is early morning in Nairobi, the Kenyan capital. The traffic jam along Ngong """
    e4 = Extractor(text=text4)
    e4.find_entities()

    assert len(e4.places) > 0
    assert 'Nairobi' in e4.places
    assert 'Ngong' in e4.places

    # unicode
    text5 = u""" There is a city called New York in the United States."""
    e5 = Extractor(text=text5)
    e5.find_entities()

    print e5.places
    assert len(e5.places) == 2
    assert u'New York' in e5.places
    assert u'United States' in e5.places

    # unicode and two words
    text6 = u""" There is a city called São Paulo in Brazil."""
    e6 = Extractor(text=text6)
    e6.find_entities()

    print e6.places
    assert len(e6.places) > 1
    assert u'São Paulo' in e6.places
