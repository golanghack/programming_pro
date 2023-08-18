#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--ASCII PUNCTUATION AND FILTRATION AND FUNCTIONALITY STYLE CODING-->"""

import string

is_ascii = lambda s: not any(map(lambda c: ord(c) >= 127, s))

is_ascii.__doc__ = """\
    >>> is_ascii("Universal suffrage")
    True
    >>> is_ascii("Cinema vérité")
    False
    """
    
is_ascii_punctuation = (lambda s: not any(map(lambda c: c not in string.punctuation, s)))
is_ascii_punctuation.__doc__ = """\
    >>> is_ascii_punctuation("No way!")
    False
    >>> is_ascii_punctuation("@!?*")
    True
    """
    
is_ascii_printable = (lambda s: not any(map(lambda c: c not in string.printable, s)))
is_ascii_printable.__doc__ = """\
    >>> is_ascii_printable("No way!")
    True
    >>> is_ascii_printable("@!?*\\t\\n")
    True
    >>> is_ascii_printable("@!?*\\t\\x05\\n")
    False
    >>> is_ascii_printable("Cinema vérité")
    False
    """
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()