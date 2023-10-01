#! /usr/bin/env python3 

import asyncio

async def consumer(condition, n):
    with await condition:
        print(f'consumer {n} is waiting ')
        await condition.wait()
        print(f'consumer {n} triggered')
    print(f'ending consumer {n}')

async def manipulate_condition(condition):
    print('starting manipulate_condition')

    # pause 
    await asyncio.sleep(.1)

    for i in range(1, 3):
        with await condition:
            print(f'notifying {i} consumers')
            condition.notify(n=1)
        await asyncio.sleep(.1)
    with await condition:
        print('notifying remaining consumers')
        condition.notify_all()
    print('ending manipulate_condition')

async def main(loop):
    # create condition
    condition = asyncio.Condition()

    # create list of tasks 
    consumers = [
        consumer(condition, i) for i in range(5)
    ]

    # plane task of manipulation of condition 
    loop.create_task(manipulate_condition(condition))

    # wait finished consumers
    await asyncio.wait(consumers)

event_loop = asyncio.get_event_loop()

try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
