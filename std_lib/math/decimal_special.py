#! /usr/bin/env python3 

import decimal

for value in ['Infinity', 'NaN', '0']:
    print(decimal.Decimal(value), decimal.Decimal('-' + value))
print()

# infinity
print('Infinity + 1 -> ', (decimal.Decimal('Infinity') + 1))
print('-Infinity + 1 -> ', (decimal.Decimal('-Infinity') + 1))

# NaN
print(decimal.Decimal('NaN') == decimal.Decimal('Infinity'))
print(decimal.Decimal('NaN') != decimal.Decimal(1))