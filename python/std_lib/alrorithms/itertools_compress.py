#! /usr/bin/env python3 

from itertools import * 

every_third = cycle([False, False, True])
every_second = cycle([False, True, False])

data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()

for j in compress(data, every_second):
    print(j, end=' ')
print()