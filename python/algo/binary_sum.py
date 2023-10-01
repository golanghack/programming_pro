#! /usr/bin/env python3 

def binary_sum(sequence: list, start: int, stop: int) -> int:
    """Return the sum of the numbers in implicit slice sequence[start: stop]."""

    if start >= stop:
        return 0 
    elif start == stop - 1:
        return sequence[start]
    else:
        middle = (start + stop) // 2 
        return binary_sum(sequence, start, middle) + binary_sum(sequence, middle, stop)
