#! /usr/bin/env python3 

import asyncio
from simple_breaker import CircuitBreaker

async def main():
    async def slow_callback():
        await asyncio.sleep(2)
        
    cb = CircuitBreaker(slow_callback, 
                            timeout=1.0, 
                            time_window=5, 
                            max_failures=2, 
                            reset_interval=5)
    for _ in range(4):
        try:
            await cb.request()
        except Exception as err:
            pass
    
    print('Sleep on 5 sec ')
    await asyncio.sleep(5)
        
    for _ in range(4):
        try:
            await cb.request()
        except Exception as err:
            pass
            
            
asyncio.run(main())