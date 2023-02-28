#! /usr/bin/env python3 

import shelve

with shelve.open('test_shelf.db') as shelve_file:
    print(shelve_file['key1'])
    shelve_file['key1']['new_value'] = 'this was not here before'
    
with shelve.open('tests_shelf.db', writeback=True) as shelve_file:
    print(shelve_file['key1'])