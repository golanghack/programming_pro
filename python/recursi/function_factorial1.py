#!/usr/bin/env python3 

"""Что вычисляет следующая функция?
func(n) = {1, if n = 0, func(n - 1)*n, if n > 0}
"""

def func(n: int):
    if n != 0:
        return  func(n - 1) * n 
    return 1

print(func(1))
print(func(5))
    