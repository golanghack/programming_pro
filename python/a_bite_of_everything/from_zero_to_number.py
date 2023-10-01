#! /usr/bin/env python3 

def from_zero_to_number(num: int) -> list:
    return [sum([i, i + 1] * 100) for i in range(num)]


