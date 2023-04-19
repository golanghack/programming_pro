#! /usr/bin/env python3 

from concurrent import futures
import os 

def task(n):
    return (n, os.getpid())

ex = futures.ProcessPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print(f'ran task {n} in process {pid}')

    