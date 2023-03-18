#! /usr/bin/env python3 

import random
import threading
import time 
import logging

def worker():
    """Worker thread function -> WTF"""

    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName) - 10s) %(message)s',
)

for i  in range(3):
    th = threading.Thread(target=worker, daemon=True)
    th.start()

main_thread = threading.main_thread()
for i in threading.enumerate():
    if i is main_thread:
        continue
    logging.debug('joining %s', i.getName())
    i.join()