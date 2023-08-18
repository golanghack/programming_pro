#! /usr/bin/env python3 

import decimal 

#set context with limit precision
c = decimal.getcontext().copy()
c.prec = 3 

# create myself const 
pi = c.create_decimal('3.1415')

# rounding const 
print('PI -> ', pi)

# result used const with global context
print('Result -> ', decimal.Decimal('2.01') * pi)
