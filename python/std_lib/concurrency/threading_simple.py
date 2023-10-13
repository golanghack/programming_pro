#! /usr/bin/env python3 

import threading

def worker():
    """Function work thread."""

    print('Worker')

threads = []
for i in range(5):
    th = threading.Thread(target=worker)
    threads.append(th)
    th.start()
    