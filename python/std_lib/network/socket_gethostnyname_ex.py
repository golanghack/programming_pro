#! /usr/bin/env python3 

import socket

HOSTS = [
    'nasa.gov', 
    'www.python.org',
    'noname',
]

for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('    Hostname -> ', name)
        print('    Aliases -> ', aliases)
        print('    Addresses -> ', addresses)
    except socket.error as message:
        print('ERR -> ', message)
    print()