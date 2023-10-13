#! /usr/bin/env python3 

""" 
A function that calculates the amount of wood if the trees
cut off at height h.
"""

def compute_wood(t: list, h: int) -> list:
    """Return uantities woods from height wood in forest."""
    
    if t == []:
        return 0
    else:
        if t[0] > h:
            return t[0] - h + compute_wood(t[1:], h)
        else:
            return compute_wood(t[1:], h)