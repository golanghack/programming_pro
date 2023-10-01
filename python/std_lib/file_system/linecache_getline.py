#! /usr/bin/env python3 

import linecache
from linecache_data import * 

filename = make_tempfile()

# choice of the same line from filename and cache
# start from 1!!!
print('SOURCE -> ')
print('{!r}'.format(lorem.split('\n')[4]))
print()
print('CACHE -> ')
print(f'{linecache.getline(filename, 5)!r}')

cleanup(filename)