#! /usr/bin/env python3 

import asyncio 

async def coroutine():
    print('in coroutine')
    return 'result'

event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(coroutine())
    print(f'it returned {return_value!r}')
finally:
    event_loop.close()

