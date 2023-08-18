#! /usr/bin/env python3 

import multiprocessing

class MyFancyClass:

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print(f'Doing something fancy in {proc_name} for {self.name}')

def worker(q):
    obj = q.get()
    obj.do_something()


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=worker, args=(queue,))
    process.start()

    queue.put(MyFancyClass('Fancy'))

    queue.close()
    queue.join_thread()
    process.join()