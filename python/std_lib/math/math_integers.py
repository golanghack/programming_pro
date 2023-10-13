#! /usr/bin/env python3

import math 

HEADINGS = ('i', 'int', 'trunck', 'floor', 'ceil')
print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format('', '', '', '', '',))

fmt = '{:5.1f} {:5.1f} {:5.1f} {:5.1f} {:5.1f}'

TEST_VALUES = [
    -1.5,
    -0.8, 
    -0.5, 
    -0.2,
    0, 
    0.2, 
    0.5, 
    0.8, 
    1,
]

for i in TEST_VALUES:
    print(fmt.format(i, int(i), math.trunc(i), math.floor(i), math.ceil(i),))