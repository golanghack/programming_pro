#! /usr/bin/env python3 

import shelve 

with shelve.open('test_shelf.db') as shelve_db:
    shelve_db['key1'] = {
        'int': 10, 
        'float': 9.5, 
        'string': 'Sample data',
        }