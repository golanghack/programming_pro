#! /usr/bin/env python3 

import pathlib 

my_path = pathlib.Path('example_dir')

print(f'Removing -> {my_path}')
my_path.rmdir()