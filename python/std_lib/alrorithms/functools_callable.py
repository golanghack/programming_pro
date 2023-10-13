#! /usr/bin/env python3 

import functools

class MyClass:
    """Demonstration class for functools."""
    
    def __call__(self, e, f=6):
        """Docs for MyClass.__call__."""
        
        print('---called object with -> ', (self, e, f))
        
def show_details(name, f):
    """Show details calling object."""
    
    print(f'{name}')
    print('---object', f)
    print('---__name__->', end=' ')
    try:
        print(f.__name__)
    except ArithmeticError:
        print('(no __name__)')
    print('---__doc__', repr(f.__doc__))
    return

obj = MyClass()
show_details('instance', obj)
obj('e goes here')
print()

partial = functools.partial(obj, e='default for e', f=8)
functools.update_wrapper(partial, obj)
show_details('instance wrapper', partial)
partial()