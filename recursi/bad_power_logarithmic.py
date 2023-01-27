#! /usr/bin/env python3 

def bad_power(b: int, n: int) -> int:
    """Bad power function."""
    
    if n == 0:
        return 1
    elif n % 2 == 0:
        return bad_power(b, n // 2) * bad_power(b, n // 2)
    else:
        #!!!BAD!!!
        return (bad_power(b, (n - 1) // 2) * bad_power(b, (n - 1) // 2) * b)
    
print(bad_power(3, 3))