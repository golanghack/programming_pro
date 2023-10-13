#! /usr/bin/env python3 

import asyncio

async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .300
    
asyncio.run(main(), debug=True)