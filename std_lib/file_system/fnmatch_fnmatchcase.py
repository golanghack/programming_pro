#! /usr/bin/env python3 

import fnmatch
import os 

pattern = 'FNMATCH_*.PY'
print('Pattern -> ', pattern)
print()

files = os.listdir('.')

for name in files:
    print(f'Filename -> {name:<25} {fnmatch.fnmatchcase(name, pattern)}')
    