#! /usr/bin/env python3

def circuit(n: int, r: int) -> int:
    if n == 1:
        return r
    else:
        return 1 / (1 / r + 1 / (circuit(n - 1, r) + r))
