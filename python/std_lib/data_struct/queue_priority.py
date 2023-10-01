#! /usr/bin/env python3 

import functools
import queue
import threading

@functools.total_ordering
class Job:
    """Class illustated work job society."""
    
    def __init__(self, priority: int, desc: str) -> None:
        self.priority = priority
        self.desc = desc
        print('New job -> ', desc)
        return 
    
    def __eq__(self, other) -> bool:
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented
        
    def __lt__(self, other) -> bool:
        try:
            return self.priority < other.priority
        except ArithmeticError:
            return NotImplemented
        
priority_job_queue = queue.PriorityQueue()

priority_job_queue.put(Job(3, 'Mid-level job'))
priority_job_queue.put(Job(10, 'Low-level job'))
priority_job_queue.put(Job(1, 'Important job'))

def process_job(priority_job_queue):
    """Function for show job."""
    
    while True:
        next_job = priority_job_queue.get()
        print('Processing job -> ', next_job.desc)
        priority_job_queue.task_done()
        
workers = [
    threading.Thread(target=process_job, args=(priority_job_queue,)),
    threading.Thread(target=process_job, args=(priority_job_queue,)),
]

for w in workers:
    w.setDaemon(True)
    w.start()
    
priority_job_queue.join()