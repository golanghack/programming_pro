#! /usr/bin/env python3 

import multiprocessing
import time 
import sys 

def daemon():
    process = multiprocessing.current_process()
    print('Starting', process.name, process.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting -> ', process.name, process.pid)
    sys.stdout.flush()

def non_daemon():
    process = multiprocessing.current_process()
    print('Startimg -> ', process.name, process.pid)
    sys.stdout.flush()
    print('Exiting -> ', process.name, process.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    daem = multiprocessing.Process(
        name='daemon', 
        target=daemon,
    )
    daem.daemon = True

    non_dem = multiprocessing.Process(
        name='non-daemon', 
        target=non_daemon,
    )
    non_dem.daemon = False

    daem.start()
    time.sleep(1)
    non_dem.start()