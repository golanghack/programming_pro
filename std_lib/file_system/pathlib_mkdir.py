#! /usr/bin/env python3 

import pathlib

my_path = pathlib.Path('example_dir')

print(f'Creating -> {my_path}')
my_path.mkdir()