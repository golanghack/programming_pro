#! /usr/bin/env python3 

import math 

print('{:^7} {:^7} {:^7}'.format('m', 'e', 'x'))
print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

INPUTS = [
    (0.8, -3), 
    (0.5, 0),
    (0.5, 3),
]

for m, e, in INPUTS:
    x = math.ldexp(m, e)
    print(f'{m:7.2f} {e:7d} {x:7.2f}')