#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


"""<--SIMPLE DECORATOR-->"""

import logging
import os
import tempfile
import functools


if __debug__:
    logger = logging.getLogger('Logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join(tempfile.gettempdir(), 'logger.log'))
    logger.addHandler(handler)
    
    def logged(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            log = 'called -> ' + function.__name__ + '('
            log += ', '.join([f'{a!r}' for a in args] 
                             + [f'{k!s}={v!r}' (k, v) for k, v in kwargs.items()])
            result = exception = None
            try:
                result = function(*args, **kwargs)
                return result
            except Exception as err:
                exception = err
            finally:
                log +=(
                    (') -> ' + str(result)) if exception is None else f') {type(exception)}: {exception}'
                )
            logger.debug(log)
            if exception is not None:
                raise exception
            return wrapper
else:
    def logged(function):
        return function
    
        