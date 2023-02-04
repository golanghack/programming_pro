#! /usr/bin/env python3 

import asyncio
from util import delay 

async def hello_every_second() -> str:
    for _ in range(2):
        await asyncio.sleep(1)
        print('I waiting while another code work!')
        
async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay
    
asyncio.run(main())

