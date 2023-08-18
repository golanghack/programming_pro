#! /usr/bin/env python3 

from itertools import * 

def show(iterable):
    first = None
    for _, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()
    
print('All permutations -> \n')
show(permutations('abcd'))

print('\nRairs -> \n')
show(permutations('abcd', r=2))