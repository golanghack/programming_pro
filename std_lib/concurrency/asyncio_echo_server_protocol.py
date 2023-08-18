#! /usr/bin/env python3 

import asyncio
import logging
import sys 


SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(name)s -> %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()

# work with client
class EchoServer(asyncio.Protocol):

    # connection new client
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger('EchoServer_{}_{}'.format(*self.address))
        self.log.debug('connection accepted')

    # Received data
    def data_received(self, data):
        self.log.debug(f'received {data!r}')
        self.transport.write(data)
        self.log.debug(f'sent {data!r}')

    
    # EOF functionality
    def eof_received(self):
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    
# create server 
# event loop break coroutine before start real event loop
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))

# infinity eventl loop for connections
try:
    event_loop.run_forever()
finally:
    log.debug('closing server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('closing event loop')
    event_loop.close()