#! /usr/bin/env python3 

import pathlib

my_path = pathlib.Path(__file__)

print(f'{my_path} is owned by {my_path.owner()} / {my_path.group()}')