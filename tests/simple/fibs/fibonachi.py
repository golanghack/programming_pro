#! /usr/bin/env python3 

M = {0: 0, 1: 1}

def fib(n:int) -> int:
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

print(fib(7))