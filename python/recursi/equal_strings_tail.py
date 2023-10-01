#! /usr/bin/env python3 

def equal_strings_tail(s: str, t: str) -> bool:
    """Return False when strinfgs not equal."""
    
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    elif s[0] != t[0]:
        return False
    else:
        return equal_strings_tail(s[1:], t[1:])
    
