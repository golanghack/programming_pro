#! /usr/bin/env python3 

import asyncio

def mark_done(future, result):
    print(f'setting future result to {result!r}')
    future.set_result(result)

event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('scheduling mark_done')
    event_loop.call_soon(mark_done, all_done, 'the result')

    print('entering event loop')
    result = event_loop.run_until_complete(all_done)
    print(f'returned result -> {result!r}')
finally:
    print('closing event loop')
    event_loop.close()

print(f'future result -> {all_done.result()!r}')

