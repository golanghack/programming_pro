#! /usr/bin/env python3 

import threading
import time 
import logging 

def daemon():
    logging.debug('STarting')
    time.sleep(.2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName) - 10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

th = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
th.start()

d.join(.1)
print('d.isAlive() -> ', d.isAlive())
th.join()