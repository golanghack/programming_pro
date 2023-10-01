#! /usr/bin/env python3 

async def say_hello():
    print('Hi')

async def say_goodbye():
    print('Bye')

async def meet_and_greet():
    await say_hello()
    await say_goodbye()

coro = meet_and_greet()
coro.send(None)
