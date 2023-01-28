#! /usr/bin/env python3 

def linear_search_tail_alt(a: list, x: int, index) -> int:
    """Return index of element in list."""
    
    if a == []:
        return - 1
    elif a[0] == x:
        return index
    else:
        return linear_search_tail_alt(a[1:], x, index + 1)
    
def linear_search_wrapper(a: list, x: int) -> None:
    return linear_search_tail_alt(a, x, 0)

