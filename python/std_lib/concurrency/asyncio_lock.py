#! /usr/bin/env python3 

import asyncio
import functools

def unlock(lock):
    print('callback releasing lock')
    lock.release()

async def coroutine1(lock):
    print('coroutine1 waiting for the lock')
    with await lock:
        print('coroutine acquired lock')
    print('corotine1 releasing lock')

async def coroutine2(lock):
    print('coroutine2 waiting for the lock')
    await lock
    try:
        print('coroutine acquired lock')
    finally:
        print('coroutine2 releasing lock')
        lock.release()

async def main(loop):
    # create and take diff lock
    lock = asyncio.Lock()
    print('acquiring the locxk before starting coroutines')
    await lock.acquire()
    print(f'lock acquired -> {lock.locked()}')

    # plane function callback for cancel lock
    loop.call_later(.1, functools.partial(unlock, lock))

    # start coroutines which use lock
    print('waiting for coroutines')
    await asyncio.wait([coroutine1(lock), coroutine2(lock)])

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()