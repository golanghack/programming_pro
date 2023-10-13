#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--SIMPLE DECORATOR AS ANNOTATIONS-->"""

import inspect
import functools

def strictly_typed(function):
    """Decoration function -> typing annotations
    """

    annotations = function.__annotations__
    arg_spec = inspect.getfullargspec(function)
    
    assert 'return' in annotations, 'missing type for return value'
    for arg in arg_spec.args + arg_spec.kwonlyargs:
        assert arg in annotations, ('missing type for parameter "' + arg + '"')
    
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        for name, arg in (list(zip(arg_spec.args, args)) + list(kwargs.items())):
            assert isinstance(arg, annotations[name]), (
                f'expected argument "{name}" of {annotations[name]} got {type(arg)}'
            )
        result = function(*args, **kwargs)
        assert isinstance(result, annotations[annotations['return']], 
                          (f'expected return {annotations["return"]} got {type(result)}')
                          )
        return result
    return wrapper


if __name__ == '__main__':
    def summ(a: int, b: int) -> int:
        return a + b
    
    print(summ(1, 2))