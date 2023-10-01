#! /usr/bin/env python3 

from concurrent import futures
import time 

def task(n):
    print(f'{n} -> sleeping')
    time.sleep(.5)
    print(f'{n} -> done')
    return n / 10 

def done(fn):
    if fn.cancelled():
        print(f'{fn.arg} -> cancelled')
    elif fn.done():
        print(f'{fn.arg} -> not cancelled')

if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main -> starting')
    tasks = []

    for i in range(10, 0, -1):
        print(f'main -> submitting {i}')
        func = ex.submit(task, i)
        func.arg = i 
        func.add_done_callback(done)
        tasks.append((i, func))

    for i, t in reversed(tasks):
        if not t.cancel():
            print(f'main -> did not cancel {i}')
    ex.shutdown()
    