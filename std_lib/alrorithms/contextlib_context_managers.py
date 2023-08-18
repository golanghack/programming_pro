#! /usr/bin/env python3 

import contextlib
from contextlib_contexmanager import make_context
class Tracker:
    """Main classfor managers context, generated errors."""
    
    def __init__(self, i: int) -> None:
        self.i = i
        
    def msg(self, s: str) -> None:
        print(f'{self.__class__.__name__}({self.i}) -> {s}')
        
    def __enter__(self) -> None:
        self.msg('entering')
        
class HandleError(Tracker):
    """If exception done -> no working with it."""
    
    def __exit__(self, *exc_details: list) -> bool:
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg(f'handing exception{exc_details[1]!r}')
        self.msg(f'exiting {received_exc}')
        return received_exc
    
class PassError(Tracker):
    """If exception send to away far."""
    
    def __exti__(self, *exc_details: list) -> bool:
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg(f'passing exception {exc_details[1]!r}')
        self.msg('exiting')
        return False
    
class ErrorOnExit(Tracker):
    """Exception generate."""
    
    def __exit__(self, *exc_details: list) -> None:
        self.msg('trhowing error')
        raise RuntimeError(f'from {self.i}')

class ErrorOnEnter(Tracker):
    """Exception generate."""
    
    def __enter__(self) -> None:
        self.msg('throwing error on enter')
        raise RuntimeError(f'from {self.i}')
    
    def __exit__(self, *exc_info: list) -> None:
        self.msg('exiting')
        

def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)
        
         
print('ONE EXAMPLE\n')
print('No errors -> ')
variable_stack([
    HandleError(1), 
    PassError(2),
])

print('\nError at the end of the context stack -> ')
variable_stack([
    HandleError(1),
    HandleError(2),
    ErrorOnExit(3),
])

print('\nError in the middle of the context stack -> ')
variable_stack([
    HandleError(1),
    PassError(2),
    ErrorOnExit(3),
    HandleError(4),
])
    
try:
    print('\nError ignored -> ')
    variable_stack([
        PassError(1),
        ErrorOnExit(2),
    ])
except RuntimeError:
    print('error handled outside of')
    