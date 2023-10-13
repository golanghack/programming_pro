#! /usr/bin/env python3 

import asyncio 
from asyncio.events import AbstractEventLoop 
from concurrent.futures import ProcessPoolExecutor as executor
from functools import partial
from typing import List

def count(limit: int) -> int:
    counter = 0
    while counter < limit:
        counter = counter + 1
    return counter

async def main() -> None:
    with executor() as process_pool:
        # partial function count
        loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [1, 2, 3, 55, 10000000]
        calls: List[partial[int]] = [partial(count, number) for number in numbers ]
        calls_coros = []
        
        for call in calls:
            calls_coros.append(loop.run_in_executor(process_pool, call))
        # wait results
        results = await asyncio.gather(*calls_coros)
        
        for result in results:
            print(result)
            
if __name__ == '__main__':
    asyncio.run(main())