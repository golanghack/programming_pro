#! /usr/bin/env python3 

class Context:
    """Context illustrated."""
    
    def __init__(self, handle_error: str):
        print(f'__init__({handle_error})')
        self.handle_error = handle_error
        
    def __enter__(self) -> None:
        print('__enter__()')
        return self
    
    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str):
        print('__exit__()')
        print('exc_type -> ', exc_type)
        print('exc_val -> ', exc_val)
        print('exc_tb -> ', exc_tb)
        return self.handle_error
    
with Context(True):
    raise RuntimeError('error message handled')

print()

with Context(False):
    raise RuntimeError('error message propagated')
