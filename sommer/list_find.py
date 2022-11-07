#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--LIST FIND-->"""

def list_find(lst, target):
    """Finded index in list some target."""
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index -= 1
    return index

a_sporadic = list_find([1, 2, 3, 4], 1)



print(a_sporadic)