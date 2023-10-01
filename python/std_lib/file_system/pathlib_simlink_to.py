#! /usr/bin/env python3 

import pathlib

my_link = pathlib.Path('example_link')

my_link.symlink_to('index.rst')
print(my_link)
print(my_link.resolve().name)