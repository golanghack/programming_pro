#! /usr/bin/env python3 

import asyncio
import functools

def set_event(event):
    print('setting event in callback')
    event.set()

async def coroutine1(event):
    print('coroutine1 waiting for event')
    await event.wait()
    print('coroutine1 triggered')

async def coroutine2(event):
    print('coroutine2 witing for event')
    await event.wait()
    print('coroutine2 triggered')

async def main(loop):
    event = asyncio.Event()
    print(f'event start state -> {event.is_set()}')
    loop.call_later(.1, functools.partial(set_event, event))
    await asyncio.wait([coroutine1(event), coroutine2(event)])
    print(f'event end state -> {event.is_set()}')

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()