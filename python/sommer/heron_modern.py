#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--HERON MODERN-->"""

from math import sqrt as sq

def heron_modern(side_a, side_b, side_c, *, units="meters"):
    """heron_modern function return area treangulum for heron formul"""
    
    s = (side_a + side_b + side_c) / 2
    area = sq(s * (s - side_a) * (s - side_b) * (s - side_c))
    return f'{area} {units}'