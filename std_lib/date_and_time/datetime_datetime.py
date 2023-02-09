#! /usr/bin/env python3

import datetime 

print('Now -> ', datetime.datetime.now())
print('Today -> ', datetime.datetime.today())
print('UTC Now -> ', datetime.datetime.utcnow())
print()

FIELDS = [
    'year', 'month', 'day',
    'hour', 'minute', 'second',
    'microsecond',
]

date_now = datetime.datetime.now()
for attr in FIELDS:
    print(f'{attr:15} -> {getattr(date_now, attr)}')