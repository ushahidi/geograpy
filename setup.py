from setuptools import setup

setup(name='geograpy',
      version='0.1',
      description='Extract place names and meta data from text or URLs',
      url='https://github.com/ushahidi/geograpy',
      author='Jonathon Morgan',
      author_email='jonathon@ushahidi.com',
      license='MIT',
      packages=['geograpy'],
      install_requires=[
            'nltk',
            'newspaper',
            'jellyfish',
            'pycountry'
      ],
      scripts=['bin/geograpy-nltk'],
      zip_safe=False)