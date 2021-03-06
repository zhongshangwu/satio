#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
from setuptools import find_packages
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = []

test_requirements = []

setup(
    author="zhongshangwu",
    author_email='zhongshangwu7@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A simple ip proxy pool",
    entry_points={
        'console_scripts': [
            'satio=satio.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='satio',
    name='satio',
    packages=find_packages(include=['satio']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zhongshangwu/satio',
    version='0.1.0',
    zip_safe=False,
)
