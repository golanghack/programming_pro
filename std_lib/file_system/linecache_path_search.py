#! /usr/bin/env python3 

import linecache
import os 

# find module linecache with path from sys.path 
module_line = linecache.getline('linecache.py', 3)
print('MODULE -> ')
print(repr(module_line))

# search module linecache
file_src = linecache.__file__
if file_src.endswith('.pyc'):
    file_src = file_src[:-1]

print('\nFILE ->')
with open(file_src, 'r', encoding='utf-8') as f:
    file_line = f.readlines()[2]
    
print(repr(file_line))
