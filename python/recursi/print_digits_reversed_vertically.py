#! /usr/bin/env python3 


def print_digitst_reversed_vertically(n: int) -> str:
    if n < 10:
        print(n)
    else:
        print(n % 10)
        print_digitst_reversed_vertically(n // 10)
        
print_digitst_reversed_vertically(1345454)