#! /usr/bin/env python3 

import asyncio
from enum import Enum

class ConnectionState(Enum):
    WAIT_UNIT = 0 
    INITIALIZING = 1
    INITIALIZED = 2 
    
class Connection:
    
    def __init__(self):
        self._state = ConnectionState.WAIT_UNIT
        self._condition = asyncio.Condition()
        
    async def initialize(self):
        await self._change_state(ConnectionState.INITIALIZING)
        print('initialize -> Initialize connection')
        await asyncio.sleep(3)
        print('initialize ->  initilazed connectiuon')
        await self._change_state(ConnectionState.INITIALIZED)
        
    async def execute(self, query: str):
        async with self._condition:
            print('execute -> Waiting initialize connection')
            await self._condition.wait_for(self._is_initialized)
            print(f'execute -> making {query}')
            await asyncio.sleep(3)
            
    async def _change_state(self, state: ConnectionState):
        async with self._condition:
            print(f'change_state -> State change from {self._state} to {state}')
            self._state = state
            self._condition.notify_all()
            
    def _is_initialized(self):
        if self._state is not ConnectionState.INITIALIZED:
            print(f'_is_initialized -> initialize connection did not finish state -> {self._state}')
            return False
        print(f'_is_initialized -> Connection initialized')
        return True
    
async def main():
    connection = Connection()
    query_one = asyncio.create_task(connection.execute('select * from table'))
    query_two = asyncio.create_task(connection.execute('select * from other_table'))
    asyncio.create_task(connection.initialize())
    
    await query_one
    await query_two
    
asyncio.run(main())