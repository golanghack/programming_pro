#! /usr/bin/env python3 

import threading
import logging 

class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName) - 10s) %(message)s',
)

for i in range(5):
    i = MyThread()
    i.start()