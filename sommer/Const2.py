#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--CONST TO PYTHON WITH NAMEDTYPLE-->

>>> Const.max
500
>>> Const.min
100
>>> Offset.id
0
>>> Offset.name
1
>>> Offset.description
2
"""

from collections import namedtuple

Const = namedtuple('_', 'min max')(100, 500)

Offset = namedtuple('_', 'id name description')(*range(3))

if __name__ == '__main__':
    import doctest
    doctest.testmod()