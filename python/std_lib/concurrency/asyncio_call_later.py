#! /usr/bin/env python3 

import asyncio

def callback(n):
    print(f'Callback {n} invioked')

async def main(loop):
    print('registering callbacks')
    loop.call_later(.2, callback, 1)
    loop.call_later(.1, callback, 2)
    loop.call_soon(callback, 3)
    await asyncio.sleep(.4)

event_loop = asyncio.get_event_loop()

try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()