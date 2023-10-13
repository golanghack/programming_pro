#! /usr/bin/env python3 

def fib(k: int) -> int:
    if k in [0, 1]:
        return k
    return fib(k - 1) + fib(k - 2)

