#! /usr/bin/env python3 


import os 
import os.path

os.chdir('/usr')

PATHS = [
    '.', 
    '..', 
    './one/two/three', 
    '../one/two/three',
]

for path in PATHS:
    print(f'{path!r:>21} -> {os.path.abspath(path)!r}')
