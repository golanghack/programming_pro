#! /usr/bin/env python3 

import linecache
from linecache_data import * 

filename = make_tempfile()

# empty string included \n 
print(f'BLANK -> {linecache.getline(filename, 6)!r}')

cleanup(filename)