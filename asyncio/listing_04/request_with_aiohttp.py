#! /usr/bin/env python3 

import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    """Fetching request for get status code."""
    
    async with session.get(url) as result:
        return result.status
    
@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        url = 'https://google.com'
        status = await fetch_status(session, url)
        print(f'State for {url} has {status}')

asyncio.run(main())