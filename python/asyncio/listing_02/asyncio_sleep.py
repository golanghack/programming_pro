#! /usr/bin/env python3 

import asyncio 

async def hello_message() -> str:
    await asyncio.sleep(2)
    return 'Hello'

async def main() -> None:
    message = await hello_message()
    print(message)
    
asyncio.run(main())