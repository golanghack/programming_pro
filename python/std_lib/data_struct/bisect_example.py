#! /usr/bin/env python3 

import bisect

#random numbers
values: list = [13, 88, 76, 24, 55, 54, 66, 76, 12, 4, 88, 55, 1]

print('New Pos Contents')
print('--- --- --------')

lst: list = []
for i in values:
    position = bisect.bisect(lst, i)
    bisect.insort(lst, i)
    print(f'{i:3} {position:3}', lst)