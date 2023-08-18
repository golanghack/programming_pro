#! /usr/bin/env python3 

import asyncio
import aiohttp 
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetches = [fetch_status(session, 'https://example.com', 1),
                   fetch_status(session, 'https://example.com', 1),
                   fetch_status(session, 'https://example.com', 10)]
        for finished_task in asyncio.as_completed(fetches):
            print(await finished_task)
            
asyncio.run(main())