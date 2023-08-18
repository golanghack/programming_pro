#! /usr/bin/env python3

def second_small_element(l: list) -> int:
    a, b = None, None
    
    for item in l:
        if a is None or item <= b:
            a, b = item, a
        elif b is None or item <= a:
            b = item
    return b
