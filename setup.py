#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = [
    'Click>=6.0',
    'click-completion>=0.2.1',
    'numpy>=1.13.1'
    # TODO: put package requirements here
]

extra_requirements = {}

setup_requirements = [
    'pytest-runner',
    # TODO(LuckyJosh): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='aoc2017',
    version='0.1.0',
    description="""Python package for my solutions for the advent of code 2017.""",
    long_description=readme,  # + '\n\n' + history,
    author="Joshua Luckey",
    author_email='joshua.luckey@udo.edu',
    url='https://github.com/LuckyJosh/advent-of-code-2017',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'aoc-2017=aoc2017.__init__:cli_entry_point',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='advent-of-code-2017',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        '(Programming Language :: Python :: 2.7)',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    extras_require=extra_requirements
)
