#! /usr/bin/env python3

import math 

HEADINGS = ('f', 's', '< 0', '> 0', '= 0')

print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format('', '', '', '', ''))

VALUES = [
    -1.0,
    0.0, 
    1.0,
    float('-inf'),
    float('inf'),
    float('-nan'),
    float('nan'),
]

for f in VALUES:
    s = int(math.copysign(1, f))
    print(f'{f:5.1f} {s:5d} {f < 0!s:5} {f > 0!s:5} {f == 0!s:5}')