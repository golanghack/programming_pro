#! /usr/bin/env python3

import hashlib
import time

# date for md5 summ 
data = open(__file__, 'rb').read()

loop_start = time.perf_counter()

for i in range(5):
    iter_start = time.perf_counter()
    h = hashlib.sha1()
    for i in range(300000):
        h.update(data)
    csum = h.digest()
    now = time.perf_counter()
    loop_elapsed = now - loop_start
    iter_elapsed = now - iter_start
    print(time.ctime(), f' -> {iter_elapsed:0.3f} {loop_elapsed:0.3f}')
