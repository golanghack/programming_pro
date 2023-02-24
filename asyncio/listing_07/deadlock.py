#! /usr/bin/env python3 

from threading import Lock, Thread 
import time

lock_a = Lock()
lock_b = Lock()

def example_A():
    # A block capturing
    with lock_a:
        print('Capture a block A')
        # wait deadblock
        time.sleep(1)
        #  block capture
        with lock_b:
            print('Capture both blocks from A')
            
def example_B():
    with lock_b:
        print('Capture block b from B')
    with lock_a:
        print('Capture both blocks')
        
thread_1 = Thread(target=example_A)
thread_2 = Thread(target=example_B)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()