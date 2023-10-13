#! /usr/bin/env python3 

class Context:
    """Context illustated."""
    
    def __init__(self) -> None:
        print('__init__()')
        
    def __enter__(self) -> None:
        print('__enter__()')
        return self
    
    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        print('__exit__()')
        
with Context():
    print('Diong work in the context.')
        
    
    