#! /usr/bin/env python3 

import multiprocessing

def worker(number):
    """Worker process"""

    print('Worker -> ', number)

if __name__ == '__main__':
    jobs = []
    for i in range(55):
        process = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(process)
        process.start()