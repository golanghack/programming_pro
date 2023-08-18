#! /usr/bin/env python3 

class WithinContext:
    """Not with."""
    
    def __init__(self, context) -> None:
        print(f'WithinContext.__init__({context})')
        
    def do_something(self) -> None:
        print('WithinContext.do_something()')
        
    def __del__(self):
        print('WithinContext.__del__')
        
class Context:
    """Context illustrated."""
    
    def __init__(self) -> None:
        print('Context.__init__()')
        
    def __enter__(self) -> WithinContext:
        print('Context.__enter__()')
        return WithinContext(self)
    
    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        print('Context.__exit__()')
        
with Context() as c:
    c.do_something()
    
    