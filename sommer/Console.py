#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CONSOLE-->
Special Utilir for work in console
"""

import sys 
import datetime

class _RangeError(Exception): pass

def get_string(message: str, 
               name: str='string', 
               default: str=None, 
               minimum_lenght: int=0, 
               maximum_lenght: int=80,
               force_lower: bool=False) -> str:
    """Return string from input moderation"""
    
    message += ': ' if default is None else f'[{default}]: '
    while True:
        try: 
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_lenght == 0:
                    return '' 
                else:
                    raise ValueError(f'{name} may not be empty')
            if not (minimum_lenght <= len(line) <= maximum_lenght):
                raise ValueError(f'{name} must be have at least {minimum_lenght} and at most {maximum_lenght} characters')
            return line if not force_lower else line.lower()
        except ValueError as err:
            print(f'!!!ERROR!!! -> {err}')
            
            
def get_integer(message: str, 
                name: str='integer', 
                default: int=None, 
                minimum: int=None, 
                maximum: int=None, 
                allow_zero: bool=True) -> int:
    """Return moderation integer"""
    
    message += ': ' if default is None else f' [{default}]: '
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            x = int(line)
            if x == 0:
                if allow_zero:
                    return x
                else:
                    raise _RangeError(f'{name} may not be 0')
            if ((minimum is not None and minimum > x) or 
                (maximum is not None and maximum < x)):
                raise _RangeError(f'{name} myst be between {minimum} and {maximum}'
                                  f'inclusive{"(or 0)" if allow_zero else ""}')
            return x 
        except _RangeError as err:
            print(f'!!!ERROR!!! -> {err}')
        except ValueError as err:
            print(f'!!!ERROR!!! {name} must be an integer')
            
            
def get_float(message: str, 
              name: str='float', 
              default: float=None, 
              minimum: float=None, 
              maximum: float=None, 
              allow_zero: bool=True) -> float:
    """Return modified float"""
    
    message += ': ' if default is None else f' [{default}]: '
    while True:
        try: 
            line = input(message)
            if not line and default is not None:
                return default
            x = float(line)
            if abs(x) < sys.float_info.epsilon:
                if allow_zero:
                    return x
                else:
                    raise _RangeError(f'{name} may not be 0.0')
            if ((minimum is not None and minimum > x) or 
                (maximum is not None and maximum < x)): 
                raise _RangeError(f'{name} must be between {minimum} and {maximum} '
                                  f'inclusive{" (or 0.0)" if allow_zero else ""}')
            return x 
        except _RangeError as err:
            print(f'!!!ERROR!!! -> {err}')
        except ValueError as err:
            print(f'ERROR {name} must be a float')
            
def get_bool(message: str, 
             default: bool=None) -> str:
    """Return modified bool"""
    
    yes = frozenset({'1', 'y', 'yes', 't', 'true', 'ok'})
    message += ' (y/yes/n/no)'
    message += ': ' if default is None else f' [{default}]: '
    line = input(message)
    if not line and default is not None:
        return default in yes
    return line.lower() in yes

def get_data(message: str, 
             default: str=None, 
             format: str='%y-%m-%d') -> str:
    """Return modified datetime """
    
    message += ': ' if default is None else f' [{default}]: '
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            return datetime.datetime.strptime(line, format)
        except ValueError as err:
            print(f'!!!ERROR!!! -> {err}')
            
            
def get_menu_choice(message: str, 
                    valid: bool,
                    default: str=None, 
                    forse_lower: bool=False) -> str:
    """Return strings menu for command in console"""
    
    message += ': ' if default is None else f'[{default}]: '
    while True:
        line = input(message)
        if not line and default is not None:
            return default
        if line not in valid:
            print('!!!ERROR!!! only {0} are valid choisces'.format(', '.join(["'{0}'".format(x)
                                                                              for x in sorted(valid)])))
        else:
            return line if not forse_lower else line.lower()
        
        
        