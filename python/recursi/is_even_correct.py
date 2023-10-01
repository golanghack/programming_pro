#! /usr/bin/env python3 

def is_even_corect(n: int) -> bool:
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even_corect(n - 2)
    