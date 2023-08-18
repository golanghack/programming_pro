#! /usr/bin/env python3 

import inspect
import string

def is_string(value: str) -> bool:
    """Trying value is string object"""
    
    return isinstance(value, str)

for name, value in inspect.getmembers(string, is_string):
    if name.startswith('_'):
        continue
    print(f'{name}s={value}r\n')
    
    