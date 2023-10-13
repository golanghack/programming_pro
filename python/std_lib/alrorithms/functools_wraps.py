#! /usr/bin/env python3 

import functools

def show_details(name: str, f: object) -> None:
    """Show details calling object."""
    
    print(f'{name}')
    print('---object -> ', f)
    print('---__name__ -> ', end=' ')
    
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('---__doc__', repr(f.__doc__))
    print()
    
def simple_decorator(f: object) -> object:
    """Super simple decorator."""
    
    @functools.wraps(f)
    def decorated(a: str='decorated defaults', b: int=1) -> object:
        print('---decorated -> ', (a, b))
        print('---', end=' ')
        return f(a, b=b)
    return decorated

def my_func(a: int, b: int=2) -> None:
    """my_func() is not complicated."""
    
    print('---my_func -> ', (a, b))
    return

# origin function
show_details('my_func', my_func)
my_func('unwrapped, dfault b')
my_func('unwrapped, passing b', 3)
print()

# compress
wrapped_my_func = simple_decorator(my_func)
show_details('wrapped_my_func', wrapped_my_func)
wrapped_my_func()
wrapped_my_func('args to wrapped', 4)
print()

# compress with decorator syntax
@simple_decorator
def decorated_my_func(a, b):
    my_func(a, b)
    return

show_details('decorated_my_func -> ', decorated_my_func)
decorated_my_func()
decorated_my_func('args to decorated, 4')
