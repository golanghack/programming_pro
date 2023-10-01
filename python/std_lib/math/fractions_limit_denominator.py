#! /usr/bin/env python3 

import fractions
import math 

print('PI -> ', math.pi)

f_pi = fractions.Fraction(str(math.pi))
print('No limit -> ', f_pi)

for i in [1, 6, 11, 60, 70, 90, 10, 110]:
    limited = f_pi.limit_denominator(i)
    print(f'{i:8} -> {limited}')