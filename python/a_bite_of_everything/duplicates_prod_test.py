#! /usr/bin/env python3

import time
from duplicates_version_1 import dup 

for i in range(5):
    number = 1000
    start = time.time()
    dup(list(range(number)))
    end = time.time()
    duration = end - start
    print(f'Duration for n = {number} -> {duration} secs.')
    
    
    