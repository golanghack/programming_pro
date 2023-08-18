#! /usr/bin/env python3 

import asyncio
from asyncio import AbstractEventLoop
import signal
from typing import Set 
from util.delay_functions import delay

def cancel_tasks():
    """Working with Signals and tasks."""
    
    print('Got a SIGINT')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Cancelling {len(tasks)} task(s)')
    [task.cancel() for task in tasks]
    
async def main() -> None:
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGILL, cancel_tasks)
    await delay(10)
    
asyncio.run(main())