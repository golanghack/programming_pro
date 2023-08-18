#! /usr/bin/env python3 

import time

def sum_k_numbers(limit: int) -> float:
    """Return full summ limit(first k) numbers."""
    
    start = time.time()
    full_summ = (limit * (limit + 1) // 2)
    end = time.time()
    full_time = f'{(end - start):.6f} sec`s'
    return full_summ, full_time
  
