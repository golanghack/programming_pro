#! /usr/bin/env python3 

import decimal

# Tuple 
tuple_decimal = (1, (1, 1), -2)

print('Input -> ', tuple_decimal)
print('Decimal -> ', decimal.Decimal(tuple_decimal))