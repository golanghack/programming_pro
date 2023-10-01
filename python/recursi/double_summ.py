#! /usr/bin/env python3 

""" Recursive Double Sum Functions ."""

def inner_summ(n: int, m: int) -> int:
    """Into summ."""
    
    if n <= 0:
        return 0
    else:
        return inner_summ(n - 1, m) + (m + n)
    
def outer_summ(m: int, n: int) -> int:
    """Out summ."""
    
    if m <= 0:
        return 0
    else:
        return outer_summ(m - 1, n) + inner_summ(n, m)
    
