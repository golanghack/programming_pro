#! /usr/bin/env python3 

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'C'}

m = collections.ChainMap(a, b)
print(m.maps)
print(f'c = {m["c"]}\n')

m.maps = list(reversed(m.maps))

print(m.maps)
print(f'c = {m["c"]}')