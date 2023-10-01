#! /usr/bin/env python3 

import asyncio
import logging
import aiohttp
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://example.com')
        bad_request = fetch_status(session, 'hhhh://')
        
        fetchers = [asyncio.create_task(good_request), 
                    asyncio.create_task(bad_request)]
        
        done, pending = await asyncio.wait(fetchers)
        
        print(f'Done tasks -> {len(done)}')
        print(f'Working tasks -> {len(pending)}')
        
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Request burn exception -> ', exc_info=done_task.exception())
asyncio.run(main())