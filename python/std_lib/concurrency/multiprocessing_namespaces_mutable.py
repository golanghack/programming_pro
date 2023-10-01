#! /usr/bin/env python3 

import multiprocessing

def producer(ns, event):
    # DON`T UPGRADE GLOBAL
    ns.my_list.append('This is the value')
    event.set()

def consumer(ns, event):
    print('Before -> ', ns.my_list)
    event.wait()
    print('After -> ', ns.my_list)

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []

    event = multiprocessing.Event()
    process = multiprocessing.Process(
        target=producer, 
        args=(namespace, event),
    )
    c = multiprocessing.Process(
        target=consumer, 
        args=(namespace, event), 
    )

    c.start()
    process.start()

    c.join()
    process.join()