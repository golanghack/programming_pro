#! /usr/bin/env python3 

import math 

print('{:^7} {:^7} {:^7}'.format('x', 'm', 'e'))
print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))

for x in [0.1, 0.5, 0.4]:
    m, e = math.frexp(x)
    print(f'{x:7.2f} {m:7.2f} {e:7.2f}')