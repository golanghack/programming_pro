#! /usr/bin/env python3 

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=44)
print('Representation -> ', bob)
print('Fields -> ', bob._fields)