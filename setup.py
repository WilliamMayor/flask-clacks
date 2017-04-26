#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Flask',
]

test_requirements = [
    'pytest',
    'coverage',
    'tox',
]

dev_requirements = [
    'Sphinx',
    'flake8',
]

extras = {
    'test': test_requirements,
    'dev': dev_requirements,
}

setup(
    name='flask-clacks',
    version='1.0.0',
    description="A man is not dead while his name is still spoken.",
    long_description=readme + '\n\n' + history,
    author="William Mayor",
    author_email='mail@williammayor.co.uk',
    url='https://github.com/WilliamMayor/flask-clacks',
    py_modules=['flask_clacks'],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    platforms='any',
    keywords='flask_clacks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python",
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extras,
)
