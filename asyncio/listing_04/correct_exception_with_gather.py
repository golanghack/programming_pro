#! /usr/bin/env python3

import asyncio
import aiohttp
from util import async_timed, fetch_status

@async_timed()
async def main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        exceptions = [res for res in results if isinstance(res, Exception)]
        successfully_results = [res for res in results if not isinstance(res, Exception)]
        
        print(f'All resulkts -> {results}')
        print(f'SUccess -> {successfully_results}')
        print(f'Exceptions -> {exceptions}')
        
asyncio.run(main())