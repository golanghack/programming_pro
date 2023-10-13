#! /usr/bin/env python3 

import collections

Person = collections.namedtuple('Person', 'name age')

pat = Person(name='Pat', age=12)
print('\nRepresentation -> ', pat)

pat.age = 33
