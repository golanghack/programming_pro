#! /usr/bin/env python3 

from merging_iterators import merge_iterators

def merge_sort(l: list):
    if len(l) > 1:
        m = len(l) // 2
        left, right = l[:m], l[m:]
        merge_sort(left)
        merge_sort(right)
        l[:] = merge_iterators(left, right)