#! /usr/bin/env python3 

import asyncio 
import logging 
from typing import Callable, Awaitable

class TooManyRetries(Exception):
    pass

async def retry(coro: Callable[[], Awaitable], 
                max_retries: int, 
                timeout: float, 
                retry_interval: float):
    for retry_num in range(0, max_retries):
        try:
            return await asyncio.wait_for(coro(), timeout=timeout)
        except Exception as err:
            logging.exception(f'In time happend exception({retry_num}), retry...', exc_info=err)
            
        await asyncio.sleep(retry_interval)
    raise TooManyRetries()
