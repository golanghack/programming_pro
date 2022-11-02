#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--STATISTICS-->"""

import collections
import math
import sys 

Statustics = collections.namedtuple('Statistics', 'mean mode median std_dev')

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f'usage --> {sys.argv[0]} file1, [file2 [... fileN]]')
    sys.exit()
    
    numbers = []
    frequencies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print("no numbers found")