#! /usr/bin/env python3 

import fractions

for n, d in [(1, 2), (2, 4), (3, 6)]:
    f = fractions.Fraction(n, d)
    print(f'{n} / {d} = {f}')