#! /usr/bin/env python3 

import array

a = array.array('i', range(5))

print('Initial -> ', a)

a.extend(range(5))
print('Extended ->', a)

print('Slice -> ', a[2:5])
print('Iterator ->')
print(list(enumerate(a)))