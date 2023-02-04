#! /usr/bin/env python3 

import asyncio
from util import delay 

async def main() -> None:
    task = asyncio.create_task(delay(10))
    
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
        
    except asyncio.exceptions.TimeoutError:
        print('Task time working > 5 seconds, comming soon end it!')
        result = await task
        print(result)
        
if __name__ == '__main__':
    asyncio.run(main())