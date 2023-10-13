#! /usr/bin/env python3 

"""Generator n string in Pascal treangle."""

def pascal(n: int) -> list:
    """N string in Pascal."""
    
    if n == 0:
        return [1]
    else:
        row = [1]
        previus_row = pascal(n - 1)
        for i in range(len(previus_row) - 1):
            row.append(previus_row[i] + previus_row[i + 1])
        row.append(1)
        return row 
    