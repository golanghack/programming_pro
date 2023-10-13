#! /usr/bin/env python3 
from compute_woods import compute_wood

""" 
Binary search algorithm for lumberjack problem.
"""

def collect_wood(t: list, wood: int, lower: int, upper: int) -> list:
    """bisect search with lumberjack task."""
    
    # middle height of wood in forest
    middle = (lower + upper) // 2
    wood_at_middle = compute_wood(t, middle)
    
    if wood_at_middle == wood or lower == upper:
        return middle
    elif lower == upper - 1:
        if compute_wood(t, upper) >= wood:
            return upper
        else:
            return lower
    elif wood_at_middle > wood:
        return collect_wood(t, wood, middle, upper)
    else:
        return collect_wood(t, wood, lower, middle - 1)
    
print(collect_wood([1, 2, 3], 3, 1, 1))