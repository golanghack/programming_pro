#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


"""<--SIMPLE CALLBACK-->

>>> strip_punctuation = make_strip_callback_function(',;:.!?')
>>> strip_punctuation('!!!')
''
"""

def make_strip_callback_function(characters: str) -> str:
    def strip_function(string: str) -> str:
        return string.strip(characters)
    return strip_function

if __name__ == '__main__':
    import doctest
    doctest.testmod()