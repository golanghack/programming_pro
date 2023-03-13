#! /usr/bin/env python3 

import asyncio
from asyncio.subprocess import Process

async def main():
    program = ['python3', 'burst_data.py']
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)
    print(f'pid -> {process.pid}')

    stdout, stderr = await process.communicate()
    print(stdout)
    print(stderr)
    print(f'process returned -> {process.returncode}')

asyncio.run(main())