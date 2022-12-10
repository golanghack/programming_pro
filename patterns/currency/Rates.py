#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--SINGLETON-->"""

import re 
import urllib.request 


_URL = 'https://www.bankofcanada.ca/stats/assets/csv/fx-seven-day.csv'


def get(refresh=False):
    if refresh:
        get.rates = {}
    if get.rates:
        return get.rates 
    with urllib.request.urlopen(_URL) as file:
        for line in file:
            line = line.rstrip().decode('utf-8')
            if not line or line.startswith(('#', 'Date')):
                continue
            name, currancy, *rest = re.split(r'\s*, \s*', line)
            key = f'{name} ({currancy})'
            try:
                get.rates[key] = float(rest[-1])
            except ValueError as err:
                print(f'!!!ERROR!!! -> {err}: {line}')
    return get.rates
get.rates = {}

if __name__ == '__main__':
    import sys 
    if sys.stdout.isatty():
        print(get())
    else:
        print('Loaded OK')
        
        