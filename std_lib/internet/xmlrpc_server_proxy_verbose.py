#! /usr/bin/env python3 

import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:9000', verbose=True)

print('Ping -> ', server.ping())