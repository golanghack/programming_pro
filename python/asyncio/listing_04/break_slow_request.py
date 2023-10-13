#! /usr/bin/env python3 

import asyncio 
import aiohttp 
from util import fetch_status

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://www.example.com')
        api_b = fetch_status(session, 'https://www.example.com', delay=3)
        
        done, pending = await asyncio.wait([api_a, api_a], timeout=2)
        
        for task in pending:
            if task is api_b:
                print('Api B to slow, cancel!')
                task.cancel()
                
asyncio.run(main())