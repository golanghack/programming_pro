#! /usr/bin/env python3 

def addition(arg1: float, arg2: float) -> float:
    """Summator."""
    
    return arg1 + arg2

def sub_addition(*args: float) -> float:
    """Summator."""
    
    a1, a2 = args
    return a1 + a2 

def multi_addition(*args):
    total = 0
    for a in args:
        total += a
    return total


