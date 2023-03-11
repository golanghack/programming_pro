#! /usr/bin/env python3 

import asyncio 
from asyncio import Condition

async def do_work(condition: Condition):
    while True:
        print('Waiting blocking condition')
        async with condition:
            print('Blocking catch. Waiting condition perfomance')
            await condition.wait()
            print('Condition finished, again couch block condition')
            await asyncio.sleep(1)
        print('Worked, lock released')
        
async def fire_event(condition: Condition):
    while True:
        await asyncio.sleep(5)
        print('Before send push couch lock condition')
        async with condition:
            print('Catch, pushing')
            condition.notify_all()
        print('Pushed, relesing lock')
        
async def main():
    condition = Condition()
    
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))
    
asyncio.run(main())
