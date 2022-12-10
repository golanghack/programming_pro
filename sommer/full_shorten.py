#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--FULL SHORTEN-->"""

def shorten(text, lenght=25, indicator="..."):
    """shorten return text or slice copy with added indicator to end.
    
    text - any string, lenght - max length return string (with indicator)
    indicator - string added in end result for show text of arguments is sliced.
    
    DOCTESTS
    >>> shorten("The Road")
    'The Road'
    >>> shorten("No Country for Old Man", 20)
    'No Country for Ol...'
    >>> shorten("Cities of the Plain", 15, "*")
    'Cities of the *'
    """
    
    if len(text) > lenght:
        text = text[:lenght - len(indicator)] + indicator
    return text

if __name__ == "__main__":
    import doctest
    doctest.testmod()