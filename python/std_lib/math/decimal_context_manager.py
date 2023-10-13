#! /usr/bin/env python3 

import decimal 

with decimal.localcontext() as context:
    context.prec = 2
    print('Local precision -> ', context.prec)
    print('3.14 / 3 = ', (decimal.Decimal('3.14') / 3))
print()

print('Default precision -> ', decimal.getcontext().prec)
print('3.14 / 3 = ', (decimal.Decimal('3.14') / 3))