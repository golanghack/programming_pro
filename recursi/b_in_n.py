#! /usr/bin/env python3

def b_in_n(b: int, n: int) -> int:
    """Return b in pow n."""
    
    if n == 0:
        return 1
    elif n == 1:
        return b 
    elif n < 0:
        return b * b_in_n(b, n + 1)
    else:
        return b * b_in_n(b, n - 1)