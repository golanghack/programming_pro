#! /usr/bin/env python3 

""" 
iterative Hoare partitioning method.
"""

def partition_hoare(a: list, lower: int, upper: int) -> int:
    """Hoare algorithm."""
    
    if upper >= 0:
        middle = (lower + upper) // 2
        pivot = a[middle]
        a[middle] = a[lower]
        a[lower] = pivot
        
        left = lower + 1
        rigth = upper
        
        finished = False
        while not finished:
            while left <= rigth and a[left] <= pivot:
                left += 1
            while a[rigth] > pivot:
                rigth -= 1
            if left < rigth:
                aux = a[left]
                a[left] = a[rigth]
                a[rigth] = aux
            finished = left > rigth
        
        a[lower] = a[rigth]
        a[rigth] = pivot
        
        return rigth