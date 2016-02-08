import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-deterministic-tools',
    version='0.1',
    packages=['deterministic'],
    include_package_data=True,
    license='Apache License',
    description='Simple LRU cache implementation to cache functions calls.',
    long_description=README,
    url='https://github.com/jejung/python-deterministic-tools',
    author='Jean Jung',
    author_email='jean.jung@rocketmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python', 
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
