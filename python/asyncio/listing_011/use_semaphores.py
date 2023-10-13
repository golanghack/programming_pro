#! /usr/bin/env python3 

import asyncio 
from asyncio import Semaphore

async def operation(semaphore: Semaphore):
    print('Waiting possible catch semaphore')
    async with semaphore:
        print('Catch')
        await asyncio.sleep(2)
    print('semaphore free')
    
async def main():
    semaphore = Semaphore(2)
    await asyncio.gather(*[operation(semaphore) for _ in range(4)])
    
asyncio.run(main())