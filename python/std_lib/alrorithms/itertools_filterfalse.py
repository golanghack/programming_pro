#! /usr/bin/env python3 

from itertools import * 

def check_item(x: int):
    print('Testing -> ', x)
    return x < 1

for i in filterfalse(check_item, [-1, 1, 0, 2, -2]):
    print('Yielding -> ', i)
    