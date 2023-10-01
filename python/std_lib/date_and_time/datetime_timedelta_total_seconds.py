#! /usr/bin/env python3 

import datetime

for delta in [datetime.timedelta(microseconds=1), 
              datetime.timedelta(milliseconds=1), 
              datetime.timedelta(seconds=1),
              datetime.timedelta(minutes=1),
              datetime.timedelta(hours=1),
              datetime.timedelta(days=1),
              datetime.timedelta(weeks=1),
              ]:
    print(f'{str(delta):15} = {delta.total_seconds():8}')