#! /usr/bin/env python3 

from itertools import * 

def make_iterable_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']
    
for i in chain.from_iterable(make_iterable_to_chain()):
    print(i, end=' ')
print()