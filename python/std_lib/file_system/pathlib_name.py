#! /usr/bin/env python3 

import pathlib 

use_path = pathlib.PurePosixPath('./std_lib/fyle_system/pathlib_name.py')
print(f'path -> {use_path}')
print(f'name -> {use_path.name}')
print(f'suffix -> {use_path.suffix}')
print(f'stem -> {use_path.stem}')