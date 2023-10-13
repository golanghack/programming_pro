#! /usr/bin/env python3 

def insertion_sort(l: list) -> None:
    n = len(l)
    for i in range(n):
        for j in range(n - i - 1, n - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]