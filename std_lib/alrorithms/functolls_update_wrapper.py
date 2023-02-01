#! /usr/bin/env python3 

import functools

def my_func(a: str, b: int=2):
    """Docs."""
    print('---called my_func -> ', (a, b))
    
def show_details(name: str, f: object) -> None:
    """Show details call object."""
    
    print(f'--{name}---')
    print('---object---', f)
    print('---__name__---', end=' ')
    try:
        print(f.__name__)
    except ArithmeticError:
        print('(no __name__)')
        
    print('---__doc__---', repr(f.__doc__))
    print()

show_details('my_func', my_func)

p1 = functools.partial(my_func, b=4)
show_details('raw wrapper', p1)

print('Updating wrapper -> ')
print('---asign -> ', functools.WRAPPER_ASSIGNMENTS)
print('---update -> ', functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, my_func)
show_details('updated wrapper -> ', p1)

