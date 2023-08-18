#! /usr/bin/env python3 

import asyncio 
import time 

def callback(n, loop):
    print(f'callback {n} invoked {loop.time()}')

async def main(loop):
    now = loop.time()
    print(f'clock time -> {time.time()}')
    print(f'loop time -> {now}')

    print('registering callbacks')
    loop.call_at(now + .2, callback, 1, loop)
    loop.call_at(now + .1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)

event_loop = asyncio.get_event_loop()
try:
    print('entereing event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
