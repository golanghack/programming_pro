#! /usr/bin/env python3 

import collections

#right
d1 = collections.deque()
d1.extend('abcdefg')
print('Extends -> ', d1)
d1.append('h')
print('append -> ', d1)

#left 
d2 = collections.deque()
d2.extendleft(range(6))
print('Extend left -> ', d2)
d2.appendleft(6)
print('append left -> ', d2)