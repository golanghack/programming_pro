#! /usr/bin/env python3 

import shelve

with shelve.open('test_shelf.db') as shelve_db:
    existing = shelve_db['key1']
    
print(existing)