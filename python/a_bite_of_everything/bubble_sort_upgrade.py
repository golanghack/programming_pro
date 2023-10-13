#! /usr/bin/env python3 

def bubble_sort(l: list) -> None:
    keeping = True
    while keeping:
        keeping = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                keeping = True