#! /usr/bin/env python3 

import threading
lock = threading.RLock()

print('Frist try -> ', lock.acquire())
print('Second try -> ', lock.acquire())