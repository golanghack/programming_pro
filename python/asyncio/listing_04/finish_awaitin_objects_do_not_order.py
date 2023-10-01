#! /usr/bin/env python3 

import asyncio
from util import delay 

async def main() -> None:
    results = await asyncio.gather(delay(3), delay(1))
    print(results)
print()
asyncio.run(main())