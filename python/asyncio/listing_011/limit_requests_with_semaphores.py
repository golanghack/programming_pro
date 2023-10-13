#! /usr/bin/env python3 

import asyncio  
from asyncio import Semaphore
from aiohttp import ClientSession

async def get_url(url: str, session: ClientSession, semaphore: Semaphore):
    print('Waiting possible catch semaphore')
    async with semaphore:
        print('Catch, requesting')
        response = await session.get(url)
        print('Request finished')
        return response.status
    
    
async def main():
    semaphore = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_url('https://www.example.com', session, semaphore) for _ in range(1000)]
        await asyncio.gather(*tasks)
        
asyncio.run(main())
    