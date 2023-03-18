#! /usr/bin/env python3 

import threading
import time 
import logging 

def wait_for_event(event):
    """Wait set event before do it something."""

    logging.debug('wait_for_event starting')
    event_is_set = event.wait()
    logging.debug('event set -> %s', event_is_set)

def wait_for_event_timeout(event, period):
    """Wait period seconds and will finish on timeout."""

    while not event.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = event.wait(period)
        logging.debug('event set ->,%s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName) - 10s) %(message)s',
)

event = threading.Event()
th1 = threading.Thread(name='block', target=wait_for_event, args=(event,),)
th1.start()

th2 = threading.Thread(name='nonblock', target=wait_for_event_timeout, args=(event, 2),)
th2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(.3)
event.set()
logging.debug('Event is set')