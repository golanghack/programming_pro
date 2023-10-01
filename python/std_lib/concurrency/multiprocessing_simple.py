#! /usr/bin/env python3 

import multiprocessing 

def worker():
    """Worker def"""

    print('<---Worker--->')

if __name__ == '__main__':
    jobs = []
    for i in range(55):
        process = multiprocessing.Process(target=worker)
        jobs.append(process)
        process.start()