#!/usr/bin/env python3 

def sum_first_naturals(n: int) -> int:
    """return summ natural numbers"""
    
    if n == 1:
        return 1
    elif n % 2 == 0:
        return (2 * sum_first_naturals(n / 2) + (n / 2) ** 2)
    else:
        return ((2 * sum_first_naturals(n - 1) / 2) + ((n + 1) / 2) ** 2)
    
print(sum_first_naturals(7))