#! /usr/bin/env python3 

import pathlib

use_path = pathlib.Path('..')

for f in use_path.rglob('pathlib_*.py'):
    print(f)