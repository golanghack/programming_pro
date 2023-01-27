#! /usr/bin/env python3 

"""Is palindrom?"""

def is_palindrom(s: str) -> bool:
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and is_palindrom(s[1:n - 1])

