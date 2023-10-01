#! /usr/bin/env python3 

import asyncio
import random 
import string 
import time
from asyncio.subprocess import Process

async def encrypt(text: str) -> bytes:
    program = ['gpg', '-c', '--batch', '--passphrase', 'encryptm3', '--cipher-algo', 'TWOFISH']

    process: Process = await asyncio.create_subprocess_exec(*program, 
                                                stdout=asyncio.subprocess.PIPE, 
                                                stdin=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate(text.encode())
    return stdout

async def main():
    text_list = [''.join(random.choice(string.ascii_letters) for _ in range(1000)) for _ in range(10)]
    start = time.time()
    tasks = [asyncio.create_task(encrypt(text)) for text in text_list]
    encrypted_text = await asyncio.gather(*tasks)
    end = time.time()

    print(f'time work -> {end - start} sec.')
    print(encrypted_text)

asyncio.run(main())

