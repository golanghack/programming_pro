#! /usr/bin/env python3 

import asyncio
from util import delay

async def main():
    while True:
        delay_time = input('Enter time for sleep -> ')
        asyncio.create_task(delay(int(delay_time)))
        
asyncio.run(main())