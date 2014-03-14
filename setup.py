from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-basemaps',
	version=version,
	description="Switch Geo-maps plugin for CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Geospatial Information Authority of Japan',
	author_email='',
	url='http://ckan.gsi.go.jp',
	license='FreeBSD',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.basemaps'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.basemaps:PluginClass
	mapbases_layer=ckanext.basemaps.plugin:LayerBasemapsPlugin
	""",
)
