#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--GREP WITH SUBPROCESS-->"""

import sys 

#maximum lenght of word
BLOCK_SIZE = 8000

#debug varible number
number = f'{sys.argv[1]}' if len(sys.argv) == 2 else ''
stdin = sys.stdin.buffer.read()
lines = stdin.decode('utf8', 'ignore').splitlines()
word = lines[0].rstrip()

for filename in lines[1:]:
    filename = filename.rstrip()
    previous = ''
    try:
        with open(filename, 'rb') as fh:
            while True:
                current = fh.read(BLOCK_SIZE)
                if not current:
                    break
                current = current.decode('utf8', 'ignore')
                if (word in current or word in previous[-len(word):] + current[:len(word)]):
                    print(f'{number}{filename}')
                    break
                if len(current) != BLOCK_SIZE:
                    break
                previous = current
    except EnvironmentError as err:
        print(f'{number}{err}')