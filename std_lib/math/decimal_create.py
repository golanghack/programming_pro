#! /usr/bin/env python3 

import decimal 

fmt = '{0:<25} {1:<25}'

print(fmt.format('Input', 'Output'))
print(fmt.format('-' * 25, '-' * 25))

# integer
print(fmt.format(5, decimal.Decimal(5)))

# string 
print(fmt.format('3.14', decimal.Decimal(3.14)))

# float 
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print(f'{f:<0.23g} {str(decimal.Decimal.from_float(f))[:25]}')