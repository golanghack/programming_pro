#! /usr/bin/env python3 

import dbm 
import shelve

with shelve.open('test_shelf.db', flag='r') as shelve_db:
    print('Existing -> ', shelve_db['key1'])
    try:
        shelve_db['key1'] = 'new value'
    except dbm.error as err:
        print(f'!!!ERRORR!!! -> {err}')