#! /usr/bin/env python3

"""Skip space in strings""" 

def skip_space(string: str, idx: int):
    while idx < len(string) and string[idx].isspace():
        idx += 1
    return idx