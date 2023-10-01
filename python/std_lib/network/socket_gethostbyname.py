#! /usr/bin/env python3 

import socket

HOSTS = [
    'apu', 'nasa.gov', 'www.python.org',
]

for host in HOSTS:
    try:
        print(f'{host} -> {socket.gethostbyname(host)}')
    except socket.error as message:
        print(f'{host} -> {message}')