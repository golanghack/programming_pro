#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue, PriorityQueue
from dataclasses import dataclass, field

@dataclass(order=True)
class WorkItem:
    priority: int 
    data: str = field(compare=False)
    
async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f'Working {work_item}')
        queue.task_done()
        
async def main():
    priority_queue = PriorityQueue()
    
    work_items = [WorkItem(3, 'Low'), 
                  WorkItem(2, 'Med'), 
                  WorkItem(1, 'High'),]
    
    worker_task = asyncio.create_task(worker(priority_queue))
    
    for work in work_items:
        priority_queue.put_nowait(work)
    
    await asyncio.gather(priority_queue.join(), worker_task)
    
asyncio.run(main())