#! /usr/bin/env python3 

import asyncio 
import aiohttp 
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)), 
                    asyncio.create_task(fetch_status(session, url)), 
                    asyncio.create_task(fetch_status(session, url, delay=3))]
        done, pending = await asyncio.wait(fetchers, timeout=2)
        
        print(f'Done tasks -> {len(done)}')
        print(f'Waiting tasks -> {len(pending)}')
        
        for done_task in done:
            result = await done_task
            print(result)
            
asyncio.run(main())
        