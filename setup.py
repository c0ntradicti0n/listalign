from setuptools import setup


install_requires = []

tests_require = [
    'texttable',
    'paired',
    'matplotlib'
    ]

setup(
   name='listalign',
   version='1.0',
   description='Align lists of strings, that sum up to the same string, by a suffix tree',
   author='Stefan Werner',
   author_email='stefan.renrew@gmail.com',
   packages=['listalign'],
   install_requires= install_requires,
   tests_require = tests_require,
   package_dir={"":"python/listalign"}
)
