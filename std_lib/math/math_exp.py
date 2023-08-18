#! /usr/bin/env python3 

import math 

fmt = '{:.20f}'

print(fmt.format(math.e ** 2))
print(fmt.format(math.pow(math.e, 2)))
print(fmt.format(math.exp(2)))