#! /usr/bin/env python3 

import contextlib

def callback(*args, **kwargs) -> None:
    print(f'closing callback({args}, {kwargs})')
    
try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'arg1', 'arg2')
        stack.callback(callback, arg3='val3')
        raise RuntimeError('trhow error')
except RuntimeError as err:
    print(f'ERROR -> {err}')