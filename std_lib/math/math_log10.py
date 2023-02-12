#! /usr/bin/env python3 

import math

print('{:2} {:^12} {:^10} {:^20} {:8}'.format('i', 'x', 'accurate', 'inaccurate', 'mismatch'))
print('{:-^2} {:-^12} {:-^10} {:-^20} {:-^8}'.format('', '', '', '', ''))

for i in range(0, 10):
    x = math.pow(10, i)
    accurate = math.log10(x)
    inaccurate = math.log(x, 10)
    match = '' if int(inaccurate) == i else '*'
    print(f'{i:2d} {x:12.1f} {accurate:10.8f} {inaccurate:20.18f} {match:^5}')
