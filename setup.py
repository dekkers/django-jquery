#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'django-jquery',
    version = '0.1.11',
    description = "Django app - bundles jQuery for django-staticfiles",
    long_description = open('README.rst').read(),
    author = 'Aljosa Mohorovic',
    author_email = 'aljosa.mohorovic@gmail.com',
    url='http://github.com/aljosa/django-jquery/',
    packages = find_packages(),
    include_package_data = True,
    license = "MIT License",
    keywords = "django jquery staticfiles",
    platforms = ['any'],
)
