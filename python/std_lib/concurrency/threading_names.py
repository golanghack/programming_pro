#! /usr/bin/env python3 

import threading
import time 

def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(.2)
    print(threading.current_thread().getName(), 'Exiting')

def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(.3)
    print(threading.current_thread().getName(), 'Exiting')

th = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
th.start()