#! /usr/bin/env python3 

import functools

def my_func(a: str, b: int=2) -> None:
    """Docs for my_func()."""
    
    print('------called my_func with -> ', (a, b))
    
def show_details(name: str, f: object, is_partial: bool) -> None:
    """Show detail calls object."""
    
    print(f'{name} -> ')
    print(f'    object -> ', f)
    if not is_partial:
        print('   __name__ -> ', f.__name__)
    if is_partial:
        print('   func -> ', f.func)
        print('   args -> ', f.args)
        print('   keywords -> ', f.keywords)
    return

show_details('my_func', my_func, True)
my_func('a', 3)
print()

# set a new default 'b' 
# must be call code return 'a'
p1 = functools.partial(my_func, b=4)
show_details('partial with named default', p1, True)
p1('passing a')
p1('override b', b=5)
print()

# a new default 'a' and 'b'
p2 = functools.partial(my_func, 'default a', b=99)
show_details('partial with defaults', p2, True)
p2()
p2(b='override b')
print()

print('Insufficient arguments ->')
p1()
    