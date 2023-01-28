#! /usr/bin/env python3 

def equal_strings(s: str, t: str) -> bool:
    """Return False for strings not equalk and True else."""
    
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    else:
        return s[0] == t[0] and equal_strings(s[1:], t[1:])
    
