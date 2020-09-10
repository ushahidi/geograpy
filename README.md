# This project is no longer being maintained and has been archived. Please check the Forks list for newer versions.

## Forks
We are aware of two 3rd party forks for this library: 
- [Maintained] https://github.com/somnathrakshit/geograpy3: recently revived, this project will be ensuring maintanance of Geograpy.Thanks to @WolfgangFahl for getting in touch about maintaining this. 
- [Outdated] This fork fixes issues with newer versions of nltk. A rewrite that fixes more issues is available here, please use it instead: https://github.com/Corollarium/geograpy2

Geograpy
========

Extract place names from a URL or text, and add context to those names -- for 
example distinguishing between a country, region or city. 

## Install & Setup

Grab the package using `pip` (this will take a few minutes)

    pip install geograpy

Geograpy uses [NLTK](http://www.nltk.org/) for entity recognition, so you'll also need 
to download the models we're using. Fortunately there's a command that'll take 
care of this for you. 

    geograpy-nltk

## Basic Usage

Import the module, give some text or a URL, and presto.

    import geograpy
    url = 'http://www.bbc.com/news/world-europe-26919928'
    places = geograpy.get_place_context(url=url)

Now you have access to information about all the places mentioned in the linked 
article. 

* `places.countries` _contains a list of country names_
* `places.regions` _contains a list of region names_
* `places.cities` _contains a list of city names_
* `places.other` _lists everything that wasn't clearly a country, region or city_

Note that the `other` list might be useful for shorter texts, to pull out 
information like street names, points of interest, etc, but at the moment is 
a bit messy when scanning longer texts that contain possessive forms of proper 
nouns (like "Russian" instead of "Russia").

## But Wait, There's More

In addition to listing the names of discovered places, you'll also get some 
information about the relationships between places.

* `places.country_regions` _regions broken down by country_
* `places.country_cities` _cities broken down by country_
* `places.address_strings` _city, region, country strings useful for geocoding_

## Last But Not Least

While a text might mention many places, it's probably focused on one or two, so 
Geograpy also breaks down countries, regions and cities by number of mentions.

* `places.country_mentions`
* `places.region_mentions`
* `places.city_mentions`

Each of these returns a list of tuples. The first item in the tuple is the place 
name and the second item is the number of mentions. For example:

    [('Russian Federation', 14), (u'Ukraine', 11), (u'Lithuania', 1)]  

## If You're Really Serious

You can of course use each of Geograpy's modules on their own. For example:

    from geograpy import extraction

    e = extraction.Extractor(url='http://www.bbc.com/news/world-europe-26919928')
    e.find_entities()

    # You can now access all of the places found by the Extractor
    print e.places

Place context is handled in the `places` module. For example:

    from geograpy import places

    pc = places.PlaceContext(['Cleveland', 'Ohio', 'United States'])
    
    pc.set_countries()
    print pc.countries #['United States']

    pc.set_regions()
    print pc.regions #['Ohio']

    pc.set_cities()
    print pc.cities #['Cleveland']

    print pc.address_strings #['Cleveland, Ohio, United States']

And of course all of the other information shown above (`country_regions` etc) 
is available after the corresponding `set_` method is called.


## Credits

Geograpy uses the following excellent libraries:

* [NLTK](http://www.nltk.org/) for entity recognition
* [newspaper](https://github.com/codelucas/newspaper) for text extraction from HTML
* [jellyfish](https://github.com/sunlightlabs/jellyfish) for fuzzy text match
* [pycountry](https://pypi.python.org/pypi/pycountry) for country/region lookups

Geograpy uses the following data sources:

* [GeoLite2](http://dev.maxmind.com/geoip/geoip2/geolite2/) for city lookups
* [ISO3166ErrorDictionary](https://github.com/bodacea/countryname/blob/master/countryname/databases/ISO3166ErrorDictionary.csv) for common country mispellings _via [Sara-Jayne Terp](https://github.com/bodacea)_

Hat tip to [Chris Albon](https://github.com/chrisalbon) for the name.
