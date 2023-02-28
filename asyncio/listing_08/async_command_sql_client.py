#! /usr/bin/env python3

import asyncio 
import os 
import tty 
from collections import deque
from util.async_reader_stdin import create_stdin_reader
from util.supporting_functions_for_ansi import * 
from util.reading_from_stdint_one_to_one_symbol import read_line
from util.messages_storage import MessageStore
import asyncpg
from asyncpg.pool import Pool

async def run_query(query: str, pool: Pool, message_store: MessageStore):
    async with pool.acquire() as connection:
        try:
            result = await connection.fetchrow(query)
            await message_store.apped(f'Choice {len(result)} strings for quesry {query}')
        except Exception as err:
            await message_store.apped(f'Got exceprion -> {err} from {query}')
            
async def main():
    tty.setcbreak(0)
    os.system('clear')
    rows = move_to_bottom_of_screen()
    
    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_bottom_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()
    
        messages = MessageStore(redraw_output, rows - 1)
        stdin_reader = await create_stdin_reader()
        
        async with asyncpg.create_pool(host='127.0.0.1', 
                                       port=5432, 
                                       user='postgres', 
                                       password='password', 
                                       database='products', 
                                       min_size=6, 
                                       max_size=6) as pool:
            while True:
                query = await read_line(stdin_reader)
                asyncio.create_task(run_query(query, pool, messages))
                
asyncio.run(main())
    

