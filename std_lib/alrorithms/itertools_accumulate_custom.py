#! /usr/bin/env python3 

from itertools import * 

def f(a: int, b: int) -> int:
    print(a, b)
    return b + a + b 

print(list(accumulate('abcde', f)))