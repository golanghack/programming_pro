#! /usr/bin/env python3 

import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from util import async_timed

from requessts_with_pool_of_threads import get_status_code

@async_timed()
async def main() -> None:
    loop = asyncio.get_running_loop()
    
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example,com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)
        
asyncio.run(main())