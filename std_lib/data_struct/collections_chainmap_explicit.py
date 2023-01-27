#! /usr/bin/env python3 

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print(f'm1["c"] = {m1["c"]}')
print(f'm2["c"] = {m2["c"]}')