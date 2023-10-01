#! /usr/bin/env python3 

"""Calculation of a polynomial according to Horner's scheme."""

def horner(c: list, x: int) -> list:
    """Calculation of a polynomial."""
    
    if len(c) == 1:
        return c[0]
    else:
        return c[0] + x * horner(c[1:], x)
