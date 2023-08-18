#! /usr/bin/env python3 

import asyncio 
from asyncio.subprocess import Process

async def main():
    process: Process = await asyncio.create_subprocess_exec('ls', '-l')
    print(f'pid process -> {process.pid}')
    status_code = await process.wait()
    print(f'Status code -> {status_code}')

asyncio.run(main())