#! /usr/bin/env python3 

def fibonacci(n: int) -> int:
    """recursi find fibonacci number."""
    
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

