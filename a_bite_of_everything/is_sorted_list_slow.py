#! /usr/bin/env python3 

def is_ssorted_list_slow(l: list) -> bool:
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                return False
    return True

