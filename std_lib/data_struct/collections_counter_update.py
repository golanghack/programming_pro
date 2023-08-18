#! /usr/bin/env python3 

import collections

c = collections.Counter()
print('Initial -> ', c)

c.update('abbbscddsddnnn')
print('Sequence -> ', c)

c.update({'a': 1, 'b': 3, 'd': 4})
print('Dict -> ', c)
