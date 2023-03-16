#! /usr/bin/env python3 

import asyncio 

@asyncio.coroutine
def coroutine():
    print('Sleep')
    yield from asyncio.sleep(1)
    print('Waike up')

asyncio.run(coroutine())