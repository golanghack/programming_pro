#! /usr/bin/env python3 

import requests
import asyncio
from util import async_timed
from requessts_with_pool_of_threads import get_status_code

@async_timed()
async def main() -> None:
    urls = ['https://www.example.com' for _ in range(1000)]
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)
    
asyncio.run(main())