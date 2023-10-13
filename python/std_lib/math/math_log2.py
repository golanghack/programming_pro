#! /usr/bin/env python3 

import math 

print('{:>2} {:^5} {:^5}'.format('i', 'x', 'log2'))
print('{:-^2} {:-^5} {:-^5}'.format('', '', ''))

for i in range(0, 10):
    x = math.pow(2, i)
    result = math.log2(x)
    print(f'{i:2d} {x:5.1f} {result:5.1f}')