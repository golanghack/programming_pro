#! /usr/bin/env python3 

def reverse_iterative(sequence: list) -> None:
    """Reverse elements in sequence""" 

    start, stop = 0, len(sequence)
    while start < stop - 1:
        sequence[start], sequence[stop - 1] = sequence[stop - 1], sequence[start]
        start, stop = start + 1, stop - 1