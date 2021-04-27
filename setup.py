# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in factory_powerstations/__init__.py
from factory_powerstations import __version__ as version

setup(
	name='factory_powerstations',
	version=version,
	description='Factory Management System',
	author='Alex Tas',
	author_email='alextas@example.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
