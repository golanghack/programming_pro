#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue
import aiohttp 
from aiohttp import ClientSession
import logging 
from bs4 import BeautifulSoup as bs


class WorkItem:
    
    def __init__(self, item_depth: int, url: str) -> None:
        self.item_depth = item_depth
        self.url = url
        
async def worker( worker_id: int, 
                     queue: Queue, 
                     session: ClientSession, 
                     max_depth: int):
        print(f'Worker {worker_id}')
        while True:
            # chose from queue url-address and download
            work_item: WorkItem = await queue.get()
            print(f'Worker {worker_id} working {work_item.url}')
            await process_page(work_item, queue, session, max_depth)
            print(f'Worker {worker_id} finished {work_item.url}')
            queue.task_done()
            
async def process_page(work_item: WorkItem, 
                       queue: Queue, 
                       session: ClientSession, 
                       max_depth: int):
    # download page for url
    # find all links in page
    # put links found to queue
    try:
        response = await asyncio.wait_for(session.get(work_item.url), timeout=3)
        if work_item.item_depth == max_depth:
            print(f'Maximum deep for {work_item.url}')
        else:
            body = await response.text()
            soup = bs(body, 'html.parser')
            links = soup.find_all('a', href=True)
            
            for link in links:
                queue.put_nowait(WorkItem(work_item.item_depth + 1, link['href']))
    except Exception as err:
        logging.exception(f'ERROR for url {work_item.url}')
        
async def main():
    # create queue for 100 tasks workers for url
    start_url = 'https://example.com'
    url_queue = Queue()
    url_queue.put_nowait(WorkItem(0, start_url))
    async with aiohttp.ClientSession() as session:
        workers = [asyncio.create_task(worker(i, url_queue, session, 3))
                   for i in range(100)]
        await url_queue.join()
        [w.cancel() for w in workers]
        
        
asyncio.run(main())  
