#! /usr/bin/env python3 

import logging 
import threading
import time

def consumer(cond):
    """Waiting condition and after use resourse."""

    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resourse is availbale to consumer')

def producer(cond):
    """Setting resourse for use consumer"""

    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resourse available')
        cond.notifyAll()

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s (%(threadName) - 2s) %(message)s',
)

condition = threading.Condition()
cond_1 = threading.Thread(name='cond_1', target=consumer, args=(condition,))
cond_2 = threading.Thread(name='cond_2', target=consumer, args=(condition,))
producer_main = threading.Thread(name='producer_main', target=producer, args=(condition,))

cond_1.start()
time.sleep(.2)
cond_2.start()
time.sleep(.2)
producer_main.start()