#! /usr/bin/env python3 

def insertion_sort(l: list) -> None:
    n = len(l)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            j += 1