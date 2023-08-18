#! /usr/bin/env python3 

import asyncio
from util import delay 

async def main() -> None:
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Time out.')
        print(f'Task cancelled? {delay_task.cancelled()}')
        
if __name__ == '__main__':
    asyncio.run(main())