#! /usr/bin/env python3 

def select_sort(l: list) -> None:
    n = len(l)
    for i in range(n - 1):
        max_index = 0 
        for index in range(n - i):
            if l[index] > l[max_index]:
                max_index = index
        l[n - i - 1], l[max_index] = l[max_index], l[n - i - 1]