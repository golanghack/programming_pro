#! /usr/bin/env python3

import asyncio
import aiohttp
from util import fetch_status

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*tasks)
        print(status_codes)
        
asyncio.run(main())