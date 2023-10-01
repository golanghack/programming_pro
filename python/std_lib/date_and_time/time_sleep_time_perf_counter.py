#! /usr/bin/env python3 

import time 

template = '{} -> {:0.2f} -> {:0.2f}'

print(template.format(time.ctime(), time.time(), time.perf_counter()))

for i in range(3, 0, -1):
    print('Sleepring', i)
    time.sleep(1)
    print(template.format(time.ctime(), time.time(), time.perf_counter()))