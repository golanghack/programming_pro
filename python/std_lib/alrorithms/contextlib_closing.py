#! /usr/bin/env python3

import contextlib

class Door:
    """Closing function class illustrate."""
    
    def __init__(self) -> None:
        print('__init__()')
        self.status = 'open'
        
    def close(self) -> None:
        """close function."""
        
        print('close()')
        self.status = 'closed'
        
print('Normal example -> ')
with contextlib.closing(Door()) as door:
    print(f'Inside with statement -> {door.status}')
print(f'Outside with statement -> {door.status}')

print('\nError handling example -> ')
try:
    with contextlib.closing(Door()) as door:
        print('Raising from inside with statement')
        raise RuntimeError('Error message')
    
except Exception as err:
    print(f'Had an error -> {err}')