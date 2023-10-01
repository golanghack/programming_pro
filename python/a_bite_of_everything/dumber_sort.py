#! /usr/bin/env python3

def dumber_sort(l: list) -> None:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]