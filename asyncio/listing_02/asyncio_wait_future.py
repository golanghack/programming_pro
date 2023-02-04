#! /usr/bin/env python3 

import asyncio
from asyncio import Future


def make_request() -> Future:
    future = Future()
    # create task for set Future
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future) -> None:
    await asyncio.sleep(1) # wait 1 sec and set future mean
    future.set_result(42)
    
async def main() -> None:
    future = make_request()
    print(f'Future object is ready? -> {future.done()}')
    # stop main function while future set not done
    value = await future
    print(f'Future object is ready? -> {future.done()}')
    print(value)
    
if __name__ == '__main__':
    asyncio.run(main())