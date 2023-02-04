#! /usr/bin/env python3 

from itertools import * 

def show(iteable):
    first = None
    for _, item in enumerate(iteable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()
    
print('Unique pairs -> \n')
show(combinations_with_replacement('abcd', r=2))