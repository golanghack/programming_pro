#! /usr/bin/env python3 

import asyncio
from asyncio.subprocess import Process

async def main():
    program = ['python3', 'burst_data.py']
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)

    print(f'pid -> {process.pid}')

    return_code = await process.wait()
    print(f'Process return -> {return_code}')

asyncio.run(main())