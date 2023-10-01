#! /usr/bin/env python3 

def function(x: int) -> float:
    """Function from x."""
    
    return x * x - 2

def bisection(a: int, b: int, f: int, epsilon: int) -> float:
    """Bisection search."""
    
    z = (a + b) / 2
    if function(z) == 0 or b - a <= 2 * epsilon:
        return z
    elif(function(a) > 0 and function(z) < 0) or (function(a) < 0 and function(z) > 0):
        return bisection(a, z, f, epsilon)
    else:
        return bisection(z, b, f, epsilon)
    
# print an approximation of the square root of 2
print(bisection(0, 4, function, 10**(-10)))
    