#! /usr/bin/env python3 

import bisect

# random numbers
values = [14, 14, 56, 5, 76, 8, 8, 9, 56, 4]

print('New Poss Contents')
print('--- --- ---------')

# insert left and right
lst = []
for i in values:
    position = bisect.bisect_left(lst, i)
    bisect.insort_left(lst, i)
    print(f'{i:3} {position:3}', lst)