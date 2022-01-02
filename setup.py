import pathlib
from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='moviescraper',
   version='1.0.0',
   description='Moviescraper',
   long_description=long_description,
   author='Gurpreet Johl',
   author_email='gurpreetjohl@gmail.com',
   packages=find_packages(exclude=['tests', 'tests.*', 'data', 'data.*']),
   install_requires=pathlib.Path('requirements.txt').read_text(),  # external packages as dependencies
   scripts=[],
   package_data={'moviescraper': ['data/*.csv']},
)
