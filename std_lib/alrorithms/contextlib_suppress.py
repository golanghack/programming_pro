#! /usr/bin/env python3

import contextlib

class NonFatalError(Exception):
    """Non fatalic exceptions class."""
    
    pass

def non_idempotent_operation() -> str:
    """Raising."""
    
    raise NonFatalError('The operation failed because of existing state')

with contextlib.suppress(NonFatalError):
    print('Trying non-idempotent operation')
    non_idempotent_operation()
    print('Succeeded')
    
print('Done')
    
    