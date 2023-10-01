#! /usr/bin/env python3 

import contextlib

@contextlib.contextmanager
def make_context() -> None:
    print('Entering -> ')
    try:
        # taking out managing, but no mean
        yield
    except RuntimeError as err:
        print('!!!ERROR!!!', err)
    finally:
        print('Exiting -> ')
        
@make_context()
def normal() -> None:
    print('Inside with statement.')
    
@make_context()
def throw_error(err: str) -> str:
    raise err 

print('Normal -> ')
normal()

print('\nHamdled error -> ')
throw_error(RuntimeError('showing example of handling and error.')) 

print('\nUnhandled error -> ')
throw_error(ValueError('this exception is not handled'))