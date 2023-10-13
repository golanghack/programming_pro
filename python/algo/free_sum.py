#! /usr/bin/env python3 

from typing import List


def chank(sequence: List[int], parts_side) -> List[int]:
    if parts_side == 'left':
        parts_half = sequence[:len(sequence) // 2]
        target = []
        for i in parts_half:
            for j in parts_half:
                for k in parts_half:
                    if i + j + k == 0:
                        target.append(i)
                        target.append(j)
                        target.append(k)
                        return target
    if parts_side == 'right':
        parts_half = sequence[len(sequence) // 2:]
        target = []
        for i in parts_half:
            for j in parts_half:
                for k in parts_half:
                    if i + j + k == 0:
                        target.append(i)
                        target.append(j)
                        target.append(k)
                        return target

def freesum(nums: List[int]) -> List[List[int]]:
    result = [[chank(nums, 'left')], [chank(nums, 'right')]]
    return result

print(freesum([-2, 1, -2, -2, -1, 3]))