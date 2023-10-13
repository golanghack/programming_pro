#! /usr/bin/env python3

def reverse_string(s: str) -> str:
    """Reversed any string."""
    
    if s == '':
        return ''
    else:
        return reverse_string(s[1:]) + s[0]
    
