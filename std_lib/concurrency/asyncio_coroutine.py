#! /usr/bin/env python3 

import asyncio 

async def coroutine():
    print('In coroutine')

event_loop = asyncio.get_event_loop()
try:
    print('start')
    coro = coroutine()
    print('enter')
    event_loop.run_until_complete(coro)
finally:
    print('closing')
    event_loop.close()