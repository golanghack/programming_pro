#! /usr/bin/env python3

from multiprocessing import Pool

def say_hello(name: str) -> str:
    return f'Hello, {name}'

if __name__ == '__main__':
    with Pool() as process_pool:
        hi_one = process_pool.apply_async(say_hello, args=('One',))
        hi_two = process_pool.apply_async(say_hello, args=('Two',))
        
        print(hi_one.get())
        print(hi_two.get())