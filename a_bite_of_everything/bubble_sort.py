#! /usr/bin/env python3 

def bubble_sort(l: list) -> None:
    for iteration in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]