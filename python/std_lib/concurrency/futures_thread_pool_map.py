#! /usr/bin/env python3 

from concurrent import futures
import threading
import time 

def task(n):
    print(f'{threading.current_thread().name} -> sleeping {n}')

    time.sleep(n / 10)
    print(f'{threading.current_thread().name} -> done with {n}')
    return n / 10 

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main -> starting')
results = ex.map(task, range(5, 0, -1))
print(f'main -> unprocessed results {results}')
print('main -> waiting for real results')
real_results = list(results)
print(f'main -> results -> {real_results}')

