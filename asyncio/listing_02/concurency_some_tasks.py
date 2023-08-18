#! /usr/bin/env python3 

import asyncio
from util import delay

async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    
    await sleep_for_three
    await sleep_again
    await sleep_again
    
asyncio.run(main())