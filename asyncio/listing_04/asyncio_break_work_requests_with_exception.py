#! /usr/bin/env python3 

import aiohttp
import asyncio
import logging 
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'pp://')),
                    asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
                    asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)
        
        print(f'Done tasks -> {len(done)}')
        print(f'Waiting -> {len(pending)}')
        
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Request return exception', exc_info=done_task.exception())
        for pending_task in pending:
            pending_task.cancel()
            
asyncio.run(main())