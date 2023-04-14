#! /usr/bin/env python3 

import asyncio

async def consumer(n, q):
    print(f'consumer {n} -> starting')
    while True:
        print(f'consumer {n} -> waitingfot item')
        item = await q.get()
        print(f'consumer {n} -> has item {item}')
        if item is None:
            # None -> signal for break
            q.task_done()
            break
        else:
            await asyncio.sleep(.01 * item)
            q.task_done()
    print(f'consumer {n} -> ending')

async def producer(q, num_workers):
    print('producer -> starting')
    # added tasks in queue
    # for work imitattion
    for i in range(num_workers * 3):
        await q.put(i)
        print(f'producer -> added task {i} to the queue')
    # added in queue None as a signals for break
    print('producer -> adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer -> waiting for queue to empty')
    await q.join()
    print('producer -> ending')

async def main(loop, num_consumers):
    # Create queue with fix sizxe 
    q = asyncio.Queue(maxsize=num_consumers)

    # Consumer tasks plane
    consumers = [
        loop.create_task(consumer(i, q)) for i in range(num_consumers)
    ]

    # Producer tasks plane
    prod = loop.create_task(producer(q, num_consumers))
    # wait finish all coroutines
    await asyncio.wait(consumers + [prod])

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()