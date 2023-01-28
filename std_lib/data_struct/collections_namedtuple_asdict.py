#! /usr/bin/env python3 

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=33)
print('Representation -> ', bob)
print('As dict -> ', bob._asdict())