#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue, PriorityQueue
from typing import Tuple

async def worker(queue: Queue):
    while not queue.empty():
        work_item: Tuple[int, str] = await queue.get()
        print(f'Working with element {work_item}')
        queue.task_done()

async def main():
    priority_queue = PriorityQueue()
    work_items = [(3, 'Lowest priority'), 
                  (2, 'Medium priopity'), 
                  (1, 'High priority'),]
    worler_task = asyncio.create_task(worker(priority_queue))
    
    for work in work_items:
        priority_queue.put_nowait(work)
        
    await asyncio.gather(priority_queue.join(), worler_task)
    
asyncio.run(main())