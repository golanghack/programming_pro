#! /usr/bin/env python3 

import multiprocessing
import sys 

def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')

def worker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()

lock = multiprocessing.Lock()

worker = multiprocessing.Process(
    target=worker_with, 
    args=(lock, sys.stdout),
)

new_worker = multiprocessing.Process(
    target=worker_no_with, 
    args=(lock, sys.stderr),
)

worker.start()
new_worker.start()

worker.join()
new_worker.join()