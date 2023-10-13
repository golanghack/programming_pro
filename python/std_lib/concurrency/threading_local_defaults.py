#! /usr/bin/env python3 

import random 
import threading 
import logging

def show_value(data):
    try:
        value = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value -> %s', value)

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):

    def __init__(self, value):
        super().__init__()
        logging.debug('Initializing %r', self)
        self.value = value

logging.basicConfig(
    level=logging.DEBUG, 
    format='(%(threadName) - 10s) %(message)s',
)

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    th = threading.Thread(target=worker, args=(local_data,))
    th.start()