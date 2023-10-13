#! /usr/bin/env python3 

import asyncio 
from util import delay 

async def create_tasks_no_sleep():
    task_1 = asyncio.create_task(delay(1))
    task_2 = asyncio.create_task(delay(2))
    print('For tasks with gather -> ')
    await asyncio.gather(task_1, task_2)

async def create_tasks_sleep():
    task_1 = asyncio.create_task(delay(1))
    await asyncio.sleep(0)
    task_2 = asyncio.create_task(delay(2))
    await asyncio.sleep(0)
    print('For task with gather -> ')
    await asyncio.gather(task_1, task_2)

async def main():
    print('---Without asyncio.sleep(0) ---')
    await create_tasks_no_sleep()
    print('--- With asyncio.sleep(0) ---')
    await create_tasks_sleep()

asyncio.run(main())