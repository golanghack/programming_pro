#! /usr/bin/env python3 

import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=40)
print('\nRepresantation -> ', bob)

jane = Person(name='Jane', age=34)
print('\nField by index -> ', jane.name)

print('\nFields by index -> ')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))