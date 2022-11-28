#! /usr/bin/env python3 

import threading
from time import sleep

def sleep_sort(i):
    """SLeeping sorting"""
    
    sleep(i)
    global sortedlist
    sortedlist.append(i)
    return i 

items = [8, 6, 4, 1, 9]
sortedlist = []
ignore_result = [threading.Thread(target=sleep_sort, args=(i, )).start() for i in items]

