#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--AWFULLPOETRY-->"""

"""This program formation random sentences.
EXAMPLES:
awfulpoetry.py
her man heard politely
his boy sang
another woman hoped.
"""

import random

articles = ['a', 'an', 'the']
doings = ['be', 'have', 'do', 'say', 'go', 'take']
names = ['Peter', 'Gorg', 'Hammol', 'Bob']

try:
    get_user_line = input('Enter cost for strings --> ')
    get_user_int = int(get_user_line)
except ValueError as err:
    print(err)
    
for i in range(get_user_int):
    for art in articles:
        base = ' '
        base = base.join(random.choice(art))
        print(base, end=' ')

    

