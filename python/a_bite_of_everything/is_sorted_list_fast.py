#! /usr/bin/env python3 

def is_sorted_list_fast(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
        return True
    
    
        