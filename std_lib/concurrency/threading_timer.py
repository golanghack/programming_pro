#! /usr/bin/env python3 

import threading
import time 
import logging

def delayed():
    logging.debug('worker running')

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName)-10s) %(message)s',
)

th1 = threading.Timer(0.3, delayed)
th1.setName('th1')
th2 = threading.Timer(0.3, delayed)
th2.setName('th2')

logging.debug('starting timers')
th1.start()
th2.start()

logging.debug('waiting before cancelled %s', th2.getName())
time.sleep(.2)
logging.debug('canceling %s', th2.getName())
th2.cancel()
logging.debug('done')