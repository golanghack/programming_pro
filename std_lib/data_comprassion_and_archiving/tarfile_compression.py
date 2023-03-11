#! /usr/bin/env python3 

import tarfile
import os 

fmt = '{:<30} {:<10}'

print(fmt.format('FILENAME', 'SIZE'))
print(fmt.format('README.txt', os.stat('READMY.txt').st_size))

FILES = [
    ('tarfile_compression.tar', 'w'), 
    ('tarfile_compression.tar.gz', 'w:gz'), 
    ('tarfile_compression.tar.bz2', 'w:bz2'),
]

for filename, write_mode in FILES:
    with tarfile.open(filename, mode=write_mode) as file:
        file.add('README.txt')
        
    print(fmt.format(filename, os.stat(filename).st_size), end=' ')
    print([m.name for m in tarfile.open(filename, 'r:*').getmembers()])
    
    