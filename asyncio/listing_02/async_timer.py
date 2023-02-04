#! /usr/bon/env python3 

"""Decorator for timing coroutins."""

import functools
import time
from typing import Callable, Any 

def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'call {func} with {args}{kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} called for {total:.f} sec.')
        return wrapped
    return wrapper

