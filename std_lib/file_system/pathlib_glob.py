#! /usr/bin/env python3 

import pathlib

use_path = pathlib.Path('..')

for f in use_path.glob('*.py'):
    print(f)