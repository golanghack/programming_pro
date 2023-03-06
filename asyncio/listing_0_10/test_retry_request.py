#! /usr/bin/env python3 

import asyncio
from retry_request import retry, TooManyRetries

async def main():
    async def always_fail():
        raise Exception('WOW FAIL!')
    
    async def always_timeout():
        await asyncio.sleep(1)
    try:
        await retry(always_fail, 
                    max_retries=3, 
                    timeout=.1, 
                    retry_interval=.1)
    except TooManyRetries:
        print('To mathc long')
    try:
        await retry(always_timeout, 
                    max_retries=3, 
                    timeout=.1, 
                    retry_interval=.1)
    except TooManyRetries:
        print('Too mach trying')
        
asyncio.run(main())