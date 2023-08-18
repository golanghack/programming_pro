#! /usr/bin/env python3 

import threading

def worker(num):
    """Working thread"""

    print(f'Worker -> {num}')

threads = []

for i in range(5):
    th = threading.Thread(target=worker, args=(i, ))
    threads.append(th)
    th.start()
    