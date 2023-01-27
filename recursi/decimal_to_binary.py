#! /usr/bin/env python3 

"""Binary representation of a non-negative integer."""

def decimal_to_binary(n: int) -> int:
    """From decimal to binary."""
    
    if n < 2:
        return n 
    else:
        return 10 * decimal_to_binary(n // 2) + (n % 2)
    