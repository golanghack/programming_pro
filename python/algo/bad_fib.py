#! /usr/bin/env python3 

def bad_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number.""" 

    if n <= 1:
        return n 
    return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

