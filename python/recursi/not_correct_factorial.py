#! /usr/bin/env python3 

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n 
    
def factorial_redurant(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return factorial_redurant(n - 1) * n 

def factorial_missing_case(n: int) -> int:
    if n == 1:
        return 1
    else:
        return factorial_missing_case(n - 1) * n 
    
def factorial_no_base_case(n: int) -> int:
    return factorial_no_base_case(n - 1) * n 