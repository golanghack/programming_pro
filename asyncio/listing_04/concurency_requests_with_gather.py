#! /usr/bin/env python3

import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        # list of program for every request want to send
        requests = [fetch_status(session, url) for url in urls]
        # wait finish every requests
        status_codes = await asyncio.gather(*requests)
        print(status_codes)
        
asyncio.run(main())