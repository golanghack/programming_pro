#! /usr/bin/env python3 

import asyncio
from asyncio.subprocess import Process


async def main():
    process: Process = await asyncio.create_subprocess_exec('sleep', '3')
    print(f'pid process -> {process.pid}')
    try:
        status_code = await asyncio.wait_for(process.wait(), timeout=1.0)
        print(status_code)
    except asyncio.TimeoutError:
        print('timeout, finished hard')
        process.terminate()
        status_code = await process.wait()
        print(status_code)

asyncio.run(main())