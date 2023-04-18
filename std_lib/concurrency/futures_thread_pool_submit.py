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
f = ex.submit(task, 5)
print(f'main -> future -> {f}')
print('main -> waiting for results')
result = f.result()
print(f'main -> result -> {result}')
print(f'main -> future after result -> {f}')

