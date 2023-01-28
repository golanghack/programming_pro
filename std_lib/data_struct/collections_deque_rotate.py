#! /usr/bin/env python3 

import collections

d = collections.deque(range(10))
print('Normal -> ', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right rotation -> ', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation -> ', d)
