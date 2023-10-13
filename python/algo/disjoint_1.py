#! /usr/bin/env python3 
from typing import List

def disjoint(A: List[int], B: List[int], C: List[int]) -> bool:
    """Return True if there is no element common to all three lists.""" 

    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    # we found common value
                    return False
    # if we reach this, sets are disjoint
    return True
