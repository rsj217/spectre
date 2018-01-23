#!/usr/bin/env python
# -*- coding:utf-8 -*-


from setuptools import setup, find_packages

with open('README.md') as f:
    r = f.read()

setup(
    name='eternal',
    version='0.0.1',
    decription='data structure and algorithm in python3',
    long_description=r,
    author='rsj217',
    author_email = 'rsj217@gmail.com',
    licens='',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)