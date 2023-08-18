#! /usr/bin/env python3 

import asyncio
from asyncio import Lock
from util import delay 

async def a(lock: Lock):
    print('Coroutina a wating possible catch lock')
    async with lock:
        print('Coroutina in critical zone')
        await delay(2)
    print('Coroutina free lock')

async def b(lock: Lock):
    print('Coroutina b waiting possible catch lock')
    async with lock:
        print('Coroutina b in critical zone')
        await delay(2)
    print('Coroutina b free lock')
    
async def main():
    lock = Lock()
    await asyncio.gather(a(lock), b(lock))
    
asyncio.run(main())
