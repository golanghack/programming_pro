#! /usr/bin/env python3 

from concurrent import futures

def task(n):
    print(f'{n} starting')
    raise ValueError(f'The value {n} isd no good')

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main -> starting')
func = ex.submit(task, 5)

error = func.exception()
print(f'main -> error -> {error}')

try:
    result = func.result()
except ValueError as err:
    print(f'main saw error "{err}" when accessing result')