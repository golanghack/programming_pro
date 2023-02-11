#! /usr/bin/env python3

import asyncio
import aiohttp 
from aiohttp import ClientSession
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com')),
                    asyncio.create_task(fetch_status(session, 'https://example.com'))]
        done, pending = await asyncio.wait(fetchers)
        
        print(f'Done tasks -> {len(done)}')
        print(f'Working task wait finish -> {len(pending)}')
        
        for done_task in done:
            result = await done_task
            print(result)
            
asyncio.run(main())