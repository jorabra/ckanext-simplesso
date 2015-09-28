from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-simplesso',
    version=version,
    description="Use a header to login to CKAN",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Jørgen Abrahamsen',
    author_email='jorgen.abrahamsen@gmail.com',
    url='jorgenabrahamsen.com',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.simplesso'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points='''
        [ckan.plugins]
        simplesso=ckanext.simplesso.plugin:SimpleSSOPlugin
    ''',
)
