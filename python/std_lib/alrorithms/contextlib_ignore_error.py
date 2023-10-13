#! /usr/bin/env python3 

import contextlib

class NonFatalError(Exception): 
    """No fatalic exceprion class."""
    
    pass

def non_idempotent_operation() -> str:
    """Rasing."""
    
    raise NonFatalError('The operation failed because of existing state')

try:
    print('Trying non-idempotent operation')
    non_idempotent_operation()
    print('Succeeded')
except NonFatalError:
    pass
print('Done')