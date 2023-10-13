#! /usr/bin/env python3 

import pathlib
import shutil
import sys 
import tempfile

with tempfile.TemporaryDirectory() as directory:
    print('Unpacking archive -> ')
    shutil.unpack_archive('example.tar.gz', extract_dir=directory)
    
    print('\nCreated -> ')
    prefix_len = len(directory) + 1
    for extract in pathlib.Path(directory).rglob('*'):
        print(str(extract)[prefix_len:])