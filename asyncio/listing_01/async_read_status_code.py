#! /usr/bin/env python3 

import time 
import threading
import requests

def read_example() -> None:
    response = requests.get('https://www.google.com')
    print(response.status_code)
    
thead_one = threading.Thread(target=read_example)
thead_two = threading.Thread(target=read_example)

thead_start = time.time()

thead_one.start()
thead_two.start()

print('Work all threads!')

thead_one.join()
thead_two.join()

thread_end = time.time()

print(f'Multithreading timing -> {thread_end - thead_start:.4f} sec.')

