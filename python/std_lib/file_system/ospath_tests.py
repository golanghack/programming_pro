#! /usr/bin/env python3 

import os.path

FILENAMES = [
    __file__, 
    os.path.dirname(__file__), 
    '/', 
    './broken_link',
]

for file in FILENAMES:
    print(f'File -> {file!r}')
    print('Absolute -> ', os.path.isabs(file))
    print('Is file? -> ', os.path.isfile(file))
    print('Is dir -> ', os.path.isdir(file))
    print('Is link -> ', os.path.islink(file))
    print('Mountpoint? -> ', os.path.ismount(file))
    print('Exists? -> ', os.path.exists(file))
    print('link Exists -> ', os.path.lexists(file))
    print()