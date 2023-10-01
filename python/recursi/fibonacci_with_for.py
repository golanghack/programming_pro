#! /usr/bin/env python3 

def fibonacci_with_for(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        counter: int = 1
        for i in range(1, n - 1):
            counter += fibonacci_with_for(i)
        return counter
    
print(fibonacci_with_for(10))