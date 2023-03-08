#! /usr/bin/env python3 

import asyncio 
from asyncio import Semaphore

async def acquare(semaphore: Semaphore):
    print('Waiting possible catch semapthore')
    async with semaphore:
        print('Catch')
        await asyncio.sleep(5)
    print('free')

async def release(semaphore: Semaphore):
    print('Unit free')
    semaphore.release()
    print('Unit free made')
    
async def main():
    semaphore = Semaphore(2)
    
    print('Two catch, three free')
    await asyncio.gather(acquare(semaphore), 
                         acquare(semaphore), 
                         release(semaphore))
    print('Three catch')
    await asyncio.gather(acquare(semaphore), 
                         acquare(semaphore), 
                         acquare(semaphore))
    
asyncio.run(main())
    