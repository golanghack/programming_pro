#! /usr/bin/env python3 

import contextlib

class Context(contextlib.ContextDecorator):
    """ContextDecorator illustrated."""
    
    def __init__(self, how_used: str) -> None:
        self.how_used = how_used
        print(f'__init__({self.how_used})')
        
    def __enter__(self):
        print(f'__enter__({self.how_used})')
        
    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str):
        print(f'__exit__({self.how_used})')
        
@Context('as decorator')
def func(message: str) -> None:
    print(message)
    
print()
with Context('ads context manager'):
    print('Doing work in the context')
    
print()
func('Doing work in the wrapped function.')