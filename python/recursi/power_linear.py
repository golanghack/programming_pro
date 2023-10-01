#! /usr/bin/env python3 

""" 
Power function for non-negative powers with linear
run time
"""
def power_linear(b: int, n: int) -> int:
    """Power_linear function"""
    
    if n == 0:
        return 1
    else:
        return b * power_linear(b, n - 1)
    
print(power_linear(5, 2))