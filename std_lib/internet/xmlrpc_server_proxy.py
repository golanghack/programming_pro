#! /usr/bin/env python3 

import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:9000')
print('Ping -> ', server.ping())