# -*- coding: utf-8 -*-


from os.path import dirname, join

from setuptools import setup, find_packages

project_dir = dirname(__file__)

with open(join(project_dir, 'VERSION'), 'rb') as f:
    version = f.read().strip()

setup(
    name="httpproxy",
    version=version,
    description="httpproxy",
    author="lvjiyong",
    url="https://github.com/lvjiyong/httpproxy",
    license="GPL",
    include_package_data=True,
    packages=find_packages(exclude=()),
    long_description=open(join(project_dir, 'README')).read(),
    maintainer='lvjiyong',
    platforms=["any"],
    maintainer_email='lvjiyong@gmail.com',
    install_requires=['requests', 'configreset'],
)