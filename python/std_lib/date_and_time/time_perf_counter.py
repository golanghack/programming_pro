#! /usr/bin/env python3 

import hashlib
import time 

# md5 summ data
data = open(__file__, 'rb').read()

for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), f' -> {time.time():0.3f} {time.perf_counter()}')
    for i in range(400000):
        h.update(data)
    csumm = h.digest()