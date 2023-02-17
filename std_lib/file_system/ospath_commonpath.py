#! /usr/bin/env python3 

import os.path

PATHS = [
    '/one/two/three/four', 
    '/one/two/threefold',
    '/one/two/three/',
]

for path in PATHS:
    print('PATH -> ', path)
    
print()
print('PREFIX -> ', os.path.commonpath(PATHS))