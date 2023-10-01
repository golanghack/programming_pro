#! /usr/bin/env python3 

"""
Hoare recursi prtitrion.
"""

def partition_hoare_recursi(a: list, left: int, right: int, pivot: int) -> list:
    """Return partitioon list."""
    
    if left > right:
        return right
    else:
        if a[left] > pivot and a[right] <= pivot:
            aux = a[left]
            a[left] = a[right]
            a[right] = aux
            return partition_hoare_recursi(a, left + 1, right - 1, pivot)
        else:
            if a[left] <= pivot:
                left += 1
            if a[right] > pivot:
                right -= 1
            return partition_hoare_recursi(a, left, right, pivot)
        

