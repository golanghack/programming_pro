#! /usr/bin/env python3 

import threading
import time 

def worker(barrier):
    print(threading.current_thread().name, 
    f'waiti
    ng for barrier with {barrier.n_waiting} others')
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting')
    else:
        print(threading.current_thread().name, 'after barrier', worker_id)

NUM_THREADS = 3 

barrier = threading.Barrier(NUM_THREADS + 1)

threads =[
    threading.Thread(
        name=f'worker - {i}', 
        target=worker, 
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for i in threads:
    print(i.name, 'starting')
    i.start()
    time.sleep(.1)

barrier.abort()

for i in threads:
    i.join()