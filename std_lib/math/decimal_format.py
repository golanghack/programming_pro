#! /usr/bin/env python3 

import decimal

d = decimal.Decimal(1.1)

print('Precision -> ')
print(f'{d:.1}')
print(f'{d:.2}')
print(f'{d:.3}')
print(f'{d:.18}')

print('\nWidth and precision combined -> ')
print(f'{d:5.1f} {d:5.1g}')
print(f'{d:5.2f} {d:5.2g}')

print('\nZero padding -> ')
print(f'{d:05.1}')
print(f'{d:05.2}')
print(f'{d:05.3}')