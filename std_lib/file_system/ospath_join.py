#! /usr/bin/env python3 

import os.path

PATHS = [
    ('one', 'two', 'three'), 
    ('/', 'one', 'two', 'three'), 
    ('/one', '/two', '/three'),
]

for pieces in PATHS:
    print(f'{pieces} -> {os.path.join(*pieces)!r}')