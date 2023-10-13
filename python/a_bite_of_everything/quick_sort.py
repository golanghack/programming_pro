#! /usr/bin/env python3 

def quick(l: list):
    # base
    if len(l) < 2:
        return l[:]
    
    # divided
    pivot = l[-1]
    left = [element for element in l if element < pivot]
    right = [element for element in l if element > pivot]
    middle = [element for element in l if element == pivot]
    
    # conque 
    left_part = quick(left)
    right_part = quick(right)
    
    # merge 
    return left_part + middle + right_part

