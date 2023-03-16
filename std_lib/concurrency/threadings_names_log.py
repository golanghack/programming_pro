#! /usr/bin/env python3 

import logging
import threading
import time 

def worker():
    logging.debug('Starting')
    time.sleep(.2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(.3)
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG, 
    format='[%(levelname)s] (%(threadName) - 10s) %(message)s', 
)

th = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
th.start()