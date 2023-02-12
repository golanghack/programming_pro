#! /usr/bin/env python3 

import asyncio 
import aiohttp 
from aiohttp import ClientSession
from util import async_timed, fetch_status

@async_timed() 
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        pending = [asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url)), 
                   asyncio.create_task(fetch_status(session, url))]
        
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            
            print(f'Done tasts -> {len(done)}')
            print(f'Waiting tasks -> {len(pending)}')
            
            for done_task in done:
                print(await done_task)
                
asyncio.run(main())