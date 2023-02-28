#! /usr/bin/env python3

import asyncio 
import os 
import tty 
from collections import deque
from util.async_reader_stdin import create_stdin_reader
from util.supporting_functions_for_ansi import * 
from util.reading_from_stdint_one_to_one_symbol import read_line
from util.messages_storage import MessageStore

async def sleep(delay: int, message_store: MessageStore): 
    # add new message in storage
    await message_store.append(f'Begin delay {delay}')
    await asyncio.sleep(delay)
    await message_store.append(f'End delay {delay}')
    
async def main():
    tty.setcbreak(sys.stdin)
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
    while True:
        line = await read_line(stdin_reader)
        delay_time = int(line)
        asyncio.create_task(sleep(delay_time, messages))
        
asyncio.run(main())