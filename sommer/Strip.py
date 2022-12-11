#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--STRIP CUSTOM REALISATION-->"""

class Strip:
    
    """Remove chars in strings
    
    >>> strip_punctuation = Strip(',;:.!?')
    >>> strip_punctuation('!!!')
    ''
    """
    def __init__(self, characters: str) -> None:
        self.characters = characters
        
    def __call__(self, string: str) -> str:
        return string.strip(self.characters)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()