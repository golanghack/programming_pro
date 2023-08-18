#! /usr/bin/env python3 

import contextlib
from contextlib_context_managers import * 

def variable_stack(contexts: list):
    with contextlib.ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)
        # return method close() new stack as a function garbage
        return stack.pop_all().close
    return None

print('No Errors -> ')
cleaner = variable_stack([
    HandleError(1),
    HandleError(2),
])
cleaner()

print('\Handled error building context manager stack -> ')
try:
    cleaner = variable_stack([
        HandleError(1),
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print(f'cauth error {err}')
    
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner returned')
        
print('\nUnbaundled error building context manager stack -> ')
try:
    cleaner = variable_stack([
        PassError(1), 
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print(f'caught error {err}')
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner returned')

