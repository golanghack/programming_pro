#! /usr/bin/env python3 

import logging
import random
import threading
import time 

class Counter:

    def __init__(self, start: int=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1 
        finally:
            self.lock.release()

def worker(counter: Counter):
    for i in range(2):
        pause = random.random()
        logging.debug('sleeping -> %0.02f', pause)
        time.sleep(pause)
        counter.increment()
    logging.debug('Done')

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName) - 10s) %(message)s',
)

counter = Counter()
for i in range(2):
    th = threading.Thread(target=worker, args=(counter, ))
    th.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for th in threading.enumerate():
    if th is not main_thread:
        th.join()

logging.debug('Counter -> %d', counter.value)

