#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


readme = open('README.rst').read()

setup(
    author="Ben Lopatin",
    author_email="ben@wellfire.co",
    name='dj-form-mapper',
    version='0.1.0',
    description='Utilities for applying Django forms validation beyond standard form data.',
    long_description=readme,
    url='https://github.com/bennylope/dj-form-mapper/',
    license='MIT License',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django',
    ],
    # test_suite='tests',
    include_package_data=True,
    zip_safe=False,
)
