#! /usr/bin/env python3 

import time 
from concurrent.futures import ProcessPoolExecutor

def count(count_to: int) -> int:
    start = time.time()
    counter = 0 
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Finish counting to {count_to} for time {end - start} sec.')
    return counter

if __name__ == '__main__':
    with ProcessPoolExecutor() as process_executor:
        numbers = [1, 4, 50, 100000000]
        for result in process_executor.map(count, numbers):
            print(result)
            