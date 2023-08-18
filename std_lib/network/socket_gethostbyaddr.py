#! /usr/bin/env python3 

import socket

hostname, aliases, addresses = socket.gethostbyaddr('10.9.0.10')

print('Hostname -> ', hostname)
print('Aliases -> ', aliases)
print('Addresses -> ', addresses)