#! /usr/bin/env python3 

import asyncio
from util import delay 
from util.async_reader_stdin import create_stdin_reader

async def main():
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))
        
asyncio.run(main())