#! /usr/bin/env python3

import collections

print('From the right -> ')
d = collections.deque('ara')
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print('From the left ->')
    
print()
print('\nFrom the left -> ')
d = collections.deque(range(6))
while True:
    try:
        print(d.popleft(), end='')
    except IndexError:
        break
    
print()