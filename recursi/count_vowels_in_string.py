#! /usr/bin/env python3 

vowels: list = ['a', 'e', 'o', 'u', 'i', 'y', 'A', 'E', 'O', 'U', 'I', 'Y']

def count_vowels(a: str) -> int:
    """Return count vowels in string a."""
    counter = 0
    if len(a) == 0:
        return counter
    elif len(a) == 1 and a[0] in vowels:
        return 1
    else:
        return count_vowels(a[1:]) + counter
        
print(count_vowels('e'))
    