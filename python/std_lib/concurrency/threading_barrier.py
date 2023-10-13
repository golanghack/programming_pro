#! /usr/bin/env python3 

import threading
import time 

def worker(barrier):
    print(threading.current_thread().name, f'waiting for barrier with{barrier.n_waiting} others')
    worker_id = barrier.wait()
    print(threading.current_thread().name, 'after barrier', worker_id)

NUM_THREADS = 3 

barrier = threading.Barrier(NUM_THREADS)

threads = [
    threading.Thread(name=f'worker-{i}', target=worker, args=(barrier, ),)
    for i in range(NUM_THREADS)
]

for i in threads:
    print(i.name, 'starting')
    i.start()
    time.sleep(.1)

for i in threads:
    i.join()