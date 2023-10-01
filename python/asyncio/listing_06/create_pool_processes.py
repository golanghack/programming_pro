#! /usr/bin/env python3 

from multiprocessing import Pool

def say_hello(name: str) -> str:
    return f'Hello, {name}'

if __name__ == '__main__':
    with Pool() as process_pool:
        hi_aba = process_pool.apply(say_hello, args=('Aba',))
        hi_bob = process_pool.apply(say_hello, args=('Bob',))
        hi_Jo = process_pool.apply(say_hello, args=('Jo',))
        
        print(hi_aba)
        print(hi_bob)
        print(hi_Jo)