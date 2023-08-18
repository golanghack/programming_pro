#! /usr/bin/env python3 

from typing import List

def linear_sum(sequence: List[int], n: int) -> int:
    """Return the sum of the fists n numbers of sequence.""" 

    if n == 0:
        return 0
    return linear_sum(sequence, n - 1) + sequence[n - 1]

print(linear_sum([1, 2, 3, 4], 4))