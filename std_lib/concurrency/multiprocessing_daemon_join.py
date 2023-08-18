#! /usr/bin/env python3 

import multiprocessing
import time
import sys 

def daemon():
    name = multiprocessing.current_process().name
    print('Starting -> ', name)
    time.sleep(2)
    print('Exiting -> ', name)


def non_daem():
    name = multiprocessing.current_process().name
    print('Starting -> ', name)
    print('Exiting -> ', name)

if __name__ == '__main__':
    daem = multiprocessing.Process(
        name='daemon', 
        target=daemon, 
    )

    daem.daemon = True

    non_daem = multiprocessing.Process(
        name='non-daemon', 
        target=non_daem,
    )
    non_daem.daemon = False

    daem.start()
    time.sleep(1)
    non_daem.start()

    daem.join()
    non_daem.join()