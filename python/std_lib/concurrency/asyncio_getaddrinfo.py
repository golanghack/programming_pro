#! /usr/bin/env python3 

import asyncio
import logging
import socket
import sys 


TARGETS = [
    ('google.com', 'https'), 
    ('nasa.gov', 'https'),
    ('python.org', 'https'), 
]

async def main(loop, targets):
    for target in targets:
        info = await loop.getaddrinfo(
            *target, 
            proto = socket.IPPROTO_TCP,
        )
        for host in info:
            print(f'{target[0]:20} -> {host[4][0]}')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()