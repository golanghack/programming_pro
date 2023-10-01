#! /usr/bin/env python3 

import multiprocessing
import time 

def slow_worker():
    print('Starting worker.')
    time.sleep(.1)
    print('Finished worker.')

if __name__ == '__main__':
    process = multiprocessing.Process(target=slow_worker)
    print('BEFORE -> ', process, process.is_alive())

    process.start()
    print('DURING -> ', process, process.is_alive())

    process.terminate()
    print('TERMINATED -> ', process, process.is_alive())

    process.join()
    print('JOINED -> ', process, process.is_alive())
    