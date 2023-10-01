#! /usr/bin/env python3 

import functools
from itertools import * 
import operator
import pprint

@functools.total_ordering
class Point:
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x 
        self.y = y 
        
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __eq__(self, __o: object) -> bool:
        return (self.x, self.y) == (__o.x, __o.y)
    
    def __gt__(self, __o: object) -> bool:
        return (self.x, self.y) > (__o.x, __o.y)
    
    
# create dataset from Point
data = list(map(Point, cycle(islice(count(), 3)), islice(count(), 7)))

print('Data -> ')
pprint.pprint(data, width=35)
print()

# try groupby unsorted data from x
print('Groupby, unsorted -> ')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
    
# sorting
data.sort()
print('Sorted -> ')
pprint.pprint(data, width=35)
print()

# groupby data from x
print('Grouped, sorted -> ')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()