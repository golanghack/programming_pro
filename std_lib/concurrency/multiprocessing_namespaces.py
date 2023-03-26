#! /usr/bin/env python3 

import multiprocessing

def producer(ns, event):
    ns.value = 'This is the value'
    event.set()

def consumer(ns, event):
    try:
        print(f'Before -> {ns.value}')
    except Exception as err:
        print('Before event, error -> ', str(err))

    event.wait()
    print('After event -> ', ns.value)

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    process = multiprocessing.Process(
        target=producer, 
        args=(namespace, event),
    )
    consumer_process = multiprocessing.Process(
        target=consumer, 
        args=(namespace, event),
    )

    consumer_process.start()
    process.start()

    consumer_process.join()
    process.join()