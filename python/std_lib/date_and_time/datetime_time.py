#! /usr/bin/env python3 

import datetime

t = datetime.time(1, 2, 3)
print(t)

print(f'''
      hour -> {t.hour}
      minute -> {t.minute}
      second -> {t.second}
      microsecond -> {t.microsecond}
      tzinfo -> {t.tzinfo}''')