#! /usr/bin/env python3

def fast_pow(x: int, y: int) -> int:
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    power = fast_pow(x, y // 2)
    power *= power
    if y % 2:
        power *= x 
    return power


assert(fast_pow(2, 2) == 4)