# -*- coding: utf-8 -*-
"""Set up openmx-tools."""

from setuptools import setup, find_packages
import json

if __name__ == '__main__':
    with open('setup.json', 'r') as info:
        kwargs = json.load(info)
    setup(
        packages=find_packages(exclude=['tests*']),
        package_data={
            '': ['*'],
        },
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        **kwargs
    )