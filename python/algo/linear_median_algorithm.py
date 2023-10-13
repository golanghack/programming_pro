#! /usr/bin/env python3 

import random
import typing

def partition(sequence: typing.List[int], index_start: int, index_end: int, index: int) -> int:
    """Breaking sequence to two parts relative sequence[index]."""

    if index_start == index_end:
        return index_start
    
    # replacing 
    sequence[index], sequence[index_start] = sequence[index_start], sequence[index]
    # counters 
    i = index_start
    j = index_end + 1
    while True:
        while True:
            i += 1
            if i == index_end:
                break
            elif sequence[index_start] < sequence[i]: 
                break
    while True:
        j -= 1
        if j == index_start:
            break
        elif sequence[j] < sequence[index_start]:
            break
        elif i >= j:
            break
        sequence[i], sequence[j] = sequence[j], sequence[i]

    sequence[index_start], sequence[j] = sequence[j], sequence[index_start]
    return j 


def linear_median(sequence: typing.List[int]) -> float:
    """Fast realisation search median in list."""

    index_start = 0
    index_end = len(sequence) - 1
    middle = index_end // 2
    while index_start < index_end:
        # random hoice index
        index = random.randint(index_start, index_end)
        j = partition(sequence, index_start, index_end, index)

        if j == middle:
            return sequence[j]
        elif j < middle:
            index_start = j + 1
        else:
            index_end = j - 1
        return sequence[index_start]

def most_fast_median(sequence: list) -> float:
    """fast find median"""

    sequence = sorted(sequence)
    mediane = sequence[len(sequence) // 2]
    return mediane

