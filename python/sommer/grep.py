#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--GREP-->"""


import sys 

if len(sys.argv) < 3:
    print('usage --> grepword.py word infile1 [infile2 [... infileN]]')
    sys.exit()
    
word = sys.argv[1]
for filename in sys.argv[2:]:
    with open(filename) as file:
        for line_number, line in enumerate(file, start=1):
            if word in line:
                print(f'{filename}:{line_number}:{line.rstrip()}')