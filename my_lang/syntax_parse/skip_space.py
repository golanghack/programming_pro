#! /usr/bin/env python3

"""Skip space in strings""" 

def skip_space(string, idx):
    while True:
        save = idx
        # try to skip spaces
        while idx < len(string) and string[idx].isspace():
            idx += 1
        # try to skio a line comment
        if idx < len(string) and string[idx] == ';':
            idx += 1
            while idx < len(string) and string[idx] != '\n':
                idx += 1
        # no more sapce or comments
        if idx == save:
            break
    return idx