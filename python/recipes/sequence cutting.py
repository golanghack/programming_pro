#! /usr/bin/env python3 

"""Cutting of sequence."""

def summing__with_cutting(items: list) -> int:
    """Recursi cutting seq."""
    
    head, *tail = items
    return head + cutting(tail) if tail else head

print(cutting([1, 2, 3]))