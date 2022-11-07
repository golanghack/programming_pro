#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--STRING TEMPLATE-->"""

import string

values = {'var': 'foo'}

temp = string.Template(
    """
    Variable          : $var
    Escape            : $$
    Variable in text  : ${var}iable
    """)

print('TEMPLATE --> ', temp.substitute(values))

s = """
    Variable          : %(var)s
    Escape            : %%
    Variable in text  : %(var)siable
    """
print('INTERPOLATION --> ', s % values)


s = """
    Variable          : {var}
    Escape            : {{}}
    Variable in text  : {var}iable
    """
print('FORMAT --> ', s.format(**values))
