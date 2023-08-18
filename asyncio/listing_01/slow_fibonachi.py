#! /usr/bin/env python3 

import time

def print_fib(number: int) -> None:
    """Printing results from function fib()."""
     
    def fib(n: int) -> int:
        if n == 1:
            return 0 
        elif n == 2:
            return 1 
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) -> {fib(number)}')
    
def fib_no_threading():
    print_fib(40)
    print_fib(41)
    
start = time.time()

fib_no_threading()

end = time.time()

print(f'Time work -> {end - start:.4f} sec.')