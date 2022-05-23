from setuptools import setup


install_requires = []

tests_require = [
    'texttable',
    'paired',
    'matplotlib'
    ]

setup(
   name='listalign',
   version='1.2',
   description='Align lists of strings, that sum up to the same string, by a suffix tree',
   packages=['listalign'],
   install_requires= install_requires,
   tests_require = tests_require
)
