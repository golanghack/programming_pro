#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue
from asyncio.tasks import Task
from typing import List
from random import randrange
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()

QUEUE_KEY = 'order_queue'
TASKS_KEY = 'order_tasks'

async def process_order_worker(worker_id: int, queue: Queue):
    # choice order from queue 
    while True:
        print(f'worker {worker_id} -> waiting order')
        order = await queue.get()
        print(f'worker {worker_id} working with order {order}')
        await asyncio.sleep(order)
        print(f'worker {worker_id} finished work with order {order}')
        queue.task_done()
        
@routes.post('/order')
async def place_order(request: Request) -> Response:
    order_queue = app[QUEUE_KEY]
    # move order in queue and send to user now 
    await order_queue.put(randrange(5))
    return Response(body='Order placed')

async def create_order_queue(app: Application):
    # create queue on 10 elems and 5 workers
    print('Creating queue orders and tasks')
    queue: Queue = Queue(10)
    app[QUEUE_KEY] = queue
    app[TASKS_KEY] = [asyncio.create_task(process_order_worker(i, queue))
                      for i in range(5)]

async def destroy_queue(app: Application):
    # waiting stopping working tasks 
    order_tasks: List[Task] = app[TASKS_KEY]
    queue: Queue = app[QUEUE_KEY]
    print('Waiting finished workers in queue')
    
    try:
        await asyncio.wait_for(queue.join(), timeout=10)
    finally:
        print('Working with orders finished, brecking workers tasks.')
        [task.cancel() for task in order_tasks]
        
        
app = web.Application()
app.on_startup.append(create_order_queue)
app.on_shutdown.append(destroy_queue)

app.add_routes(routes)
web.run_app(app, port=8081)