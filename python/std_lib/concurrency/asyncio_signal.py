#! /usr/bin/env python3 

import asyncio
import functools
import os 
import signal

def signal_handler(name: str) -> None:
    print(f'signal_handler({name!r})')

event_loop = asyncio.get_event_loop()

event_loop.add_signal_handler(signal.SIGHUP,
                                functools.partial(signal_handler, name='SIGHUP'),)

event_loop.add_signal_handler(signal.SIGUSR1, 
                                functools.partial(signal_handler, name='SIGUSR!'),)

event_loop.add_signal_handler(signal.SIGINT, 
                                functools.partial(signal_handler, name='SIGINT'),)

async def send_signals():
    pid = os.getpid()
    print(f'strting send_signals for {pid}')

    for name in ['SIGHUP', 'SIGHUP', 'SIGUSR1', 'SIGINT']:
        print(f'sending {name}')
        os.kill(pid, getattr(signal, name))
        # Away manage for signal handler 
        print('yielding control')
        await asyncio.sleep(.01)
    return

try:
    event_loop.run_until_complete(send_signals())
finally:
    event_loop.close()