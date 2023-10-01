#! /usr/bin/env python3 

"""<--DECORATOR-->"""

import functools

def static_typed(*types, return_type=None):
    """Decoration static typed result call of functions"""
    
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if len(args) > len(types):
                raise ValueError('too many args')
            if len(args) < len(types):
                raise ValueError('to few args')
            for i, (arg, type_) in enumerate(zip(args, types)):
                if not isinstance(arg, type_):
                    raise ValueError(f'argument {i} must be of type {type_.__name__}')
            result = function(*args, **kwargs)
            if (return_type is not None and not isinstance(result, return_type)):
                raise ValueError(f'return value must be of type {return_type.__name__}')
            return result
        return wrapper
    return decorator


                