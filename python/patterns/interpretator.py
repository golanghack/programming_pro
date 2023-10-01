#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--INTERPRETATOR-->"""

import collections
import math 
import sys 

def global_context():
    """return context from module in full namespace"""
    
    glob_context = globals().copy()
    for name in dir(math):
        if not name.startswith('_'):
            glob_context[name] = getattr(math, name)
    return glob_context

def calc(expression, glob_context, loc_context, current):
    """Function calculator"""
    
    try:
        result = eval(expression, glob_context, loc_context)
        update(loc_context, result, current)
        print(', '.join([f'{variable}={value}' for variable, value in loc_context.items()]))
        print(f'ANSWER -> {result}')
    except Exception as err:
        print(f'!!!ERROR!!! -> {err}')
        
def update(loc_context, result, current):
    """Then current == Z begin -> A"""
    
    loc_context[current.letter] = result
    current.letter = chr(ord(current.letter) + 1)
    if current.letter > 'Z':
        current.letter = 'A'
        
if sys.version_info >= (3, 3):
    import types
    
    def main():
        quit_ = 'Cntr+Z, enter' if sys.platform.startswith('win') else 'Cntr+D'
        prompt = f'Enter an expression ({quit_}) -> '
        current = types.SimpleNamespace(letter='A')
        glob_context = global_context()
        loc_context = collections.OrderedDict()
        while True:
            try:
                expression = input(prompt)
                if expression:
                    calc(expression, glob_context, loc_context, current)
            except EOFError:
                print()
                break
else:
    
    def main():
        quit_ = 'Cntrl+Z, Enter' if sys.platform.startswith('win') else 'Cntrl+D'
        prompt = f'Enter an expression ({quit_}) -> '
        current = type('_', dict(letter='A'))()
        glob_context = global_context()
        loc_context = collections.OrderedDict()
        while True:
            try:
                expression = input(prompt)
                if expression:
                    calc(expression, glob_context, loc_context, current)
            except EOFError:
                print()
                break
if __name__ == '__main__':
    main()