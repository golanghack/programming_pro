#! /usr/bin/env python3 

from threading import Lock, Thread 
from typing import List

list_lock = Lock()

def sum_list(int_list: List[int]) -> int:
    print('Waiting block...')
    with list_lock:
        print('Caught block')
        if len(int_list) == 0:
            print('Summing finish.')
            return 0
        else:
            head, *tail = int_list
            print('Summing remainder of list')
            return head + sum_list(tail)
        
thread = Thread(target=sum_list, args=([1, 2, 3, 4, 5, 6],))
thread.start()
thread.join()