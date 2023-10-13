#! /usr/bin/env python3 

import functools

class MyObject:
    
    def __init__(self, value: str) -> None:
        
        self.value = value
        
    def __str__(self) -> str:
        return f'MyObject({self.value})'
    
    
def compare_object(a, b) -> int:
    """Old style -> python 2.1."""
    
    print(f'comparing {a} and {b}')
    if a.value < b.value:
        return -1
    elif a.vlue > b.value:
        return 1
    return 0

# function key use function cmp_to_key()
get_key = functools.cmp_to_key(compare_object)

def get_key_wrapper(obj):
    """Wrapper for get_key, may use input function."""
    
    new_key = get_key(obj)
    print(f'key_wrapper({obj}) -> {new_key!r}')
    return new_key


objects = [MyObject(x) for x in range(5, 0, -1)]
for obj in sorted(objects, key=get_key_wrapper):
    print(obj)