#! /usr/bin/env python3 

import collections

try:
    collections.namedtuple('Person', 'name class age')
except ValueError as err:
    print(err)
    
try:
    collections.namedtuple('Person', 'name age age')
except ValueError as err:
    print(err)