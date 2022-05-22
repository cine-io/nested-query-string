#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup, find_packages

packages = find_packages(exclude=['test'])
requires = []

__version__ = ''
with open('nested_query_string/version.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break

if not __version__:
    raise RuntimeError('Cannot find version information')


def data_for(filename):
    with open(filename) as fd:
        content = fd.read()
    return content


setup(
    name="nested_query_string",
    version=__version__,
    description='Generate nested query strings similar to rack and node qs',
    license='MIT',
    author='Cine.io Engineering',
    author_email='engineering@cine.io',
    url='https://github.com/cine-io/nested-query-string',
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet",
    ],
)
