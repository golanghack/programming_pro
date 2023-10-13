#! /usr/bin/env python3 

from util_for_tasks.get_number import get_number
from functools import lru_cache

n = get_number('Enter number')

@lru_cache(None)
def f(n,c,m):
    if n == 0: return c%2 == m%2
    if c==m: return 0

    h = [f(n-i**2,c+1,m) for i in range (1,int(n**0.5)+1)]

    return any (h) if (c+1)%2 == m%2 else all(h)

for m in range (1,int(n**0.5)+5,2):
    if f(n,0,m):
        print(True)
        break
    else: 
        print(False)