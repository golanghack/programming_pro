#! /usr/bin/env python3 

import asyncio
from asyncio import CancelledError
from util import delay 

async def main() -> None:
    long_task = asyncio.create_task(delay(10))
    second_elapsed = 0
    
    while not long_task.done():
        print('Task dont funished, next test acros on second.')
        await asyncio.sleep(1)
        second_elapsed += 1
        if second_elapsed == 5:
            long_task.cancel()
            
    try:
        await long_task
    except CancelledError:
        print('Our task cancelled.')
        
asyncio.run(main())