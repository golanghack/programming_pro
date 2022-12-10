#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
"""<--FIND DUP-->"""

import collections
import os
import sys 

path = sys.argv[1] if len(sys.argv) > 1 else '.'
#create dict every key in this dict is (size file, name file <-> dont have path)
#every mean dict -> is list full names files
data = collections.defaultdict(list)

#for every directory function os.walk return path to root
# and two list first -> list of subdirs second -> list of files in directory
for root, dirs, files in os.walk(path):
    for filename in files:
        fullname = os.path.join(root, filename)
        key = (os.path.getsize(fullname), filename)
        data[key].append(fullname)
#report of the duplicated files      
for size, filename in sorted(data):
    names = data[(size, filename)]
    if len(names) > 1:
        print('{filename} ({size} bytes) may be duplicated '
              '({0} files): '.format(len(names), **locals()))
        for name in names:
            print(f'\t{name}')