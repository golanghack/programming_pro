#! /usr/bin/env python3 

from itertools import * 

def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()
    
print('Repeat 2 -> \n', end=' ')
show(list(product(range(3), repeat=2)))

print('Repeat 3 -> \n', end=' ')
show(list(product(range(3), repeat=3)))