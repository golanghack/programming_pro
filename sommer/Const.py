#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CLASS CONST-->
>>> const = Const()
>>> const.limit = 591
>>> const.limit
591
>>> const.total
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Const' object has no attribute 'total'

"""


class Const:
    
    def __setattr__(self, name: str, value: str) -> None:
        if name in self.__dict__:
            raise ValueError('Cannot change a const attr')
        self.__dict__[name] = value
        
    def __delattr__(self, name: str) -> None:
        if name in self.__dict__:
            raise ValueError('cannot delete a const attr')
        raise AttributeError(f'"{self.__class__.__name__}" object has no attr "{name}"')
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()