#! /usr/bin/env python3 

import threading
import logging 

def worker_with(lock: threading.Lock()):
    with lock:
        logging.debug('Lock acwuired via with')

def worker_no_with(lock: threading.Lock()):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName) - 10s) %(message)s',
)

lock = threading.Lock()

with_lock = threading.Thread(target=worker_with, args=(lock, ))
no_with_lock = threading.Thread(target=worker_no_with, args=(lock, ))

with_lock.start()
no_with_lock.start()