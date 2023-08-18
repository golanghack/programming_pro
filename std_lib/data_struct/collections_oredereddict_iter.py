#! /usr/bin/env python3 

import collections

print('Regular dictonary -> ')

d = {}
d['b'] = 'B'
d['c'] = 'C'
d['a'] = 'A'

for k, v in d.items():
    print(k, v)
    
print('\nOredered dict ->')
d = collections.OrderedDict()
d['a'] ='A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
    print(k, v)
    