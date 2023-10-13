#! /usr/bin/env python3 

import pathlib

use_path = pathlib.PurePosixPath('/usr/local/lib')

print(f'parent -> {use_path.parent}')

print('\nhierarchy -> ')
for up in use_path.parents:
    print(up)