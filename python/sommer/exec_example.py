#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


"""<--SIMPLE EXEMPLE USED FUNCTION EXEC-->"""

import math 

#python code
code = """ 
def area_of_sphere(r: int) -> int:
    return 4 * math.pi * r ** 2
print(area_of_sphere(4))
"""

context = {}
context['math'] = math
exec(code, context)