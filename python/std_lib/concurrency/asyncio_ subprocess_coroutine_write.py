#! /usr/bin/env python3 

import asyncio
import asyncio.subprocess

async def to_uper(in_put):
    print('in to_upper')

    create = asyncio.create_subprocess_exec(
        'tr', '[:lower:]', '[:upper:]',
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    print('launching process')
    proc = await create
    print(f'pid -> {proc.pid}')

    print('communicating with process')
    stdout, stderr = await proc.communicate(in_put.encode())

    print('waiting for process to complete')
    await proc.wait()

    return_code = proc.returncode
    print(f'return code {return_code}')
    if not return_code:
        results = bytes(stdout).decode()
    else:
        results = ''
    return (return_code, results)

MESSAGE = """This message will be converted to all caps."""

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(to_uper(MESSAGE))

finally:
    event_loop.close()

if return_code:
    print(f'error exit -> {return_code}')
else:
    print(f'Original -> {MESSAGE!r}')
    print(f'Changed -> {results!r}')
