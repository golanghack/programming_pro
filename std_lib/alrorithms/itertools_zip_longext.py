#! /usr/bin/env python3 

from itertools import * 

r1 = range(13)
r2 = range(12)

print('zip stops early -> ')
print(list(zip(r1, r2)))

r1 = range(13)
r2 = range(12)

print('\nzip_longest processes all of the values -> ')
print(list(zip_longest(r1, r2, fillvalue='*')))