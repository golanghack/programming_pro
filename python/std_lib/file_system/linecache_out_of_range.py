#! /usr/bin/env python3 

import linecache
from linecache_data import * 

filename = make_tempfile()

# cache always return string 
# use empty string for point to 
# requested string does not exists
not_line= linecache.getline(filename, 5000)
print(f'NOT THERE -> {not_line!r} includes {len(not_line)} chars.')

cleanup(filename)