#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--SUM OF POWER-->"""

def sum_of_powers(*args, power=1):
    """sum_os_powers function return every arg in power
    
    >>> sum_of_powers(1)
    1
    >>> sum_of_powers(1, 1, power=3)
    2
    """
    
    result = 0
    for arg in args:
        result += arg ** power
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()