#! /usr/bin/env python3 

def selct_sort_alt(a: list) -> list:
    """Select sorting."""
    
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)
        
        return [m] + selct_sort_alt(b)
    
print(selct_sort_alt([1, 6, 2, 7, 4]))