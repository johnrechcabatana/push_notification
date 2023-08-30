from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in push_notification/__init__.py
from push_notification import __version__ as version

setup(
	name="push_notification",
	version=version,
	description="push_notification",
	author="cabatana.johnrech.g@gmail.com",
	author_email="cabatana.johnrech.g@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
