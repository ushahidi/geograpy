from setuptools import setup
import os
import sys
if sys.version_info > (2,7):
   ins = ['numpy','nltk','newspaper3k','jellyfish','pycountry']
else:
   ins = ['numpy','nltk','newspaper','jellyfish','pycountry']

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='geograpy',
      version='0.3.7',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/reach2ashish/geograpy',
      download_url ='https://github.com/reach2ashish/geograpy/tarball/0.3.4',
      author='Jonathon Morgan',
      author_email='jonathon@ushahidi.com',
      license='MIT',
      packages=['geograpy'],
      install_requires=ins,
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data = {
            'geograpy': ['data/*.csv'],
      },
      zip_safe=False)
