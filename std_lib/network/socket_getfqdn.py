#! /usr/bin/env python3 

import socket

for host in ['nasa.gov', 'python.org']:
    print(f'{host:>10} -> {socket.getfqdn(host)}')