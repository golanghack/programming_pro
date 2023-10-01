#! /usr/bin/env python3 

import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
    """Request status code."""
    
    ten_millis = aiohttp.ClientTimeout(total=1)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status
    
async def main() -> None:
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        status = await fetch_status(session, 'https://mirf.ru')
        print(status)
        
asyncio.run(main())