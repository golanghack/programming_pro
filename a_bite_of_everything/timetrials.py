#! /usr/bin/env python3 

import time

def timetrials(func, n_range, trials=10):
    """Counting time for count operation any functions."""
    
    for i in range(trials):
        start = time.time()
        func(list(range(n_range)))
        end = time.time()
        total = end - start
    print(f'average -> {total / trials:10.7f} secs  ->  {n_range}')
        