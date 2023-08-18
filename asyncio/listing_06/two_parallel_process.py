#! /usr/bin/env python3

import time
from multiprocessing import Process

def count(count_to: int) -> int:
    """Return counting number to count_to."""
    
    start = time.time()
    counter = 0 
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Ended counting{count_to} for time{end-start} sec')
    return counter

if __name__ == '__main__':
    start_time = time.time()
    
    to_one_hungred_million = Process(target=count, args=(100000000,))
    to_two_hungred_million = Process(target=count, args=(200000000,))
    
    to_one_hungred_million.start()
    to_two_hungred_million.start()
    
    to_one_hungred_million.join()
    to_two_hungred_million.join()
    
    end_time = time.time()
    print(f'Full time work {end_time - start_time} sec')