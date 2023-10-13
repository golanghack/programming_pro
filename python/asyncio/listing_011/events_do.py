#! /usr/bin/env python3 

import asyncio
import functools
from asyncio import Event 

def trigger_event(event: Event):
    print('Acrivation event')
    event.set()
    
async def do_work_on_event(event: Event):
    print('Waiting event')
    await event.wait()
    print('Working')
    await asyncio.sleep(1)
    print('Finished')
    event.clear()
    
async def main():
    event = Event()
    asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event))
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))
    
asyncio.run(main())
        