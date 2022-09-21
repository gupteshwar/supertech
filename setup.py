from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in supertech/__init__.py
from supertech import __version__ as version

setup(
	name="supertech",
	version=version,
	description="supertech",
	author="saad",
	author_email="saad.c@indictranstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
