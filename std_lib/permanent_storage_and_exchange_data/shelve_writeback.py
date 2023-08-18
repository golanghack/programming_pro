#! /usr/bin/env python3 

import shelve
import pprint 

with shelve.open('test_shelf.db', writeback=True) as shelve_db:
    print('Iniial data -> ')
    pprint.pp(shelve_db['key1'])
    
    shelve_db['key1']['new_value'] = 'this was not here before'
    print('\nModified -> ')
    pprint.pprint(shelve_db['key1'])

with shelve.open('test_shelf.db', writeback=True) as shelve_db:
    print('\nPreserved -> ')
    pprint.pprint(shelve_db['key1'])