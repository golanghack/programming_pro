#! /usr/bin/env python3 

from concurrent import futures
import time 

def task(n):
    print(f'{n} -> sleeping')
    time.sleep(.4)
    print(f'{n} -> done')
    return n / 10 

def done(func):
    if func.cancelled():
        print(f'{func.arg} -> cancelled')
    elif func.done:
        error = func.exception()
        if error:
            print(f'{func.arg} -> error returned -> {error}')
        else:
            result = func.result()
            print(f'{func.arg} -> value returned -> {result}')

if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main -> starting')
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()

    