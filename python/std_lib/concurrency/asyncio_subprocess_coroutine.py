#! /usr/bin/env python3 

import asyncio
import asyncio.subprocess


async def run_df():
    print('run_df')

    buffer = bytearray()
    create = asyncio.create_subprocess_exec('df', '-hl', stdout=asyncio.subprocess.PIPE,)
    print('launching process')
    proc = await create
    print(f'process started {proc.pid}')

    while True:
        line = await proc.stdout.readline()
        print(f'read {line!r}')
        if not line:
            print('no more output from command')
            break
        buffer.extend(line)

        print('waiting for process to comlete')
        await proc.wait()

        