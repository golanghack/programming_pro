#! /usr/bin/env python3 

import os.path

PATHS = [
     '/one/two', 
    '/one/two/', 
    '/', 
    '.',
    '', 
]

for path in PATHS:
    print(f'{path!r:>17} -> {os.path.dirname(path)!r}')