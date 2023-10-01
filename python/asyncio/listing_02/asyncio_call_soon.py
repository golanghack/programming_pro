#! /usr/bin/env python3 

import asyncio
from util import delay 

def call_later() -> None:
    print('Will call me future.')
    
async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
    
asyncio.run(main())
    
    