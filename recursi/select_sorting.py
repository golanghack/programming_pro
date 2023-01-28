#! /usr/bin/env python3 

def select_sort(a: list) -> list:
    """Select sorting"""
    
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        min_index = b.index(min(b))
        aux = b[min_index]
        b[min_index] = b[0]
        b[0] = aux
        
        return [aux] + select_sort(b[1:])
    
print(select_sort([1, 8, 3, 6, 2]))