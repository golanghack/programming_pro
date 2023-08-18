#! /usr/bin/env python3 

import datetime 

for m in [1, 0, 0.1, 0.7]:
    try:
        print(f'{m:02.1f}', datetime.time(0, 0, 0, microsecond=m))
    except TypeError as err:
        print('ERROR -> ', err)