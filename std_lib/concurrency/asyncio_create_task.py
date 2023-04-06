#! /usr/bin/env python3 


import asyncio

async def task_func():
    print('in task_func')
    return 'the result'

async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print(f'waiting for {task!r}')
    return_value = await task

    print(f'task completed {task!r}')
    print(f'return value -> {return_value!r}')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
    