#! /usr/bin/env python3 

def _reverse(sequence: list, start: int, stop: int) -> list:
    """Reverse elements in slice sequence[start:stop]."""

    if start < stop - 1:
        sequence[start], sequence[stop - 1] = sequence[stop - 1], sequence[start]
        _reverse(sequence, start+1, stop-1)
        
