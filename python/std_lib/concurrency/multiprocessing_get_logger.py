#! /usr/bin/env python3 

import multiprocessing
import logging
import sys 

def worker():
    print('Doing some work')
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()