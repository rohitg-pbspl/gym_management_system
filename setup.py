from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_management_system/__init__.py
from gym_management_system import __version__ as version

setup(
	name="gym_management_system",
	version=version,
	description="Your local Gym needs a system to track memberships. This system should handle memberships, membership types, locker allocation, group classes, professional trainer subscriptions, etc.",
	author="Scenarios",
	author_email="Your app should handle the following scenarios:",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
