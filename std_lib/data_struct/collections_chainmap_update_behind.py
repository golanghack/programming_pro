#! /usr/bin/env python3 

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print(f'Before -> {m["c"]}')
a['c'] = 'E'
print(f'After -> {m["c"]}')