#! /usr/bin/env python3 

import threading

lock = threading.Lock()

print('First try -> ', lock.acquire())
print('Second try -> ', lock.acquire(0))