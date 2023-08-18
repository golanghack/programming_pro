#! /usr/bin/env python3 

strings = 'aaaa bbbb aaa zzzz aaaa ddd dd ff gggg rrr'.split()

def my_key(strings: str):
    return -len(strings), strings.upper()

print(sorted(strings, key=my_key))