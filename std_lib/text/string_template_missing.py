#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--STRING TEMPLATE MISSING-->"""

import string

values = {'var': 'foo'}

template = string.Template('$var is here but $missing is not provided')

try:
    print('substitute() --> ', template.substitute(values))
except KeyError as err:
    print('Error --> ', str(err))
    
print('safe_substitute() --> ', template.safe_substitute(values))