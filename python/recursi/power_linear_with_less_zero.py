#! /usr/bin/env python3 

def power_linear_with_less_zero(b: int, n: int) -> int:
    """Power linear function with less zero."""
    
    if n == 0:
        return 1
    elif n > 0:
        return b * power_linear_with_less_zero(b, n - 1)
    else:
        return power_linear_with_less_zero(b, n + 1) / b
    
