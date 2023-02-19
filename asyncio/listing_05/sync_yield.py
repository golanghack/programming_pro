#! /usr/bin/env python3 

def positive_integers(until: int) -> None:
    for integer in range(until):
        yield integer
        
positive_iterator = positive_integers(3)

print(next(positive_iterator))
print(next(positive_iterator))