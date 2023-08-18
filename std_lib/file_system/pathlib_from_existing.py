#! /usr/bin/env python3 

import pathlib

individual = pathlib.PurePosixPath('source/pathlib/index.rst')
print(individual)

python = individual.with_name('pathlib_from_existing.py')
print(python)

cpython = python.with_suffix('.pyc')
print(cpython)