#! /usr/bin/env python3 

import contextlib

@contextlib.contextmanager
def make_context(i) -> None:
    print(f'{i} entering')
    yield {}
    print(f'{i} exiting')
    
def variable_stack(n: int, msg: str) -> None:
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)
        
variable_stack(2, 'inside context')