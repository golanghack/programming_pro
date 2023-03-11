#! /usr/bin/env python3 

import asyncio
from asyncio.queues import Queue

async def main():
    custormer_queue = Queue()
    custormer_queue.get_nowait()
    
asyncio.run(main())