#! /usr/bin/env python3 

import zlib 
import logging 
import socketserver
import binascii

BLOCK_SIZE = 64 

class ZlibRequestHandler(socketserver.BaseRequestHandler):
    
    loggger = logging.getLogger('Server')
    
    def handle(self) -> None:
        compressor = zlib.compressobj(1)
        
        # file for client
        filename = self.request.recv(1024).decode('utf-8')
        self.loggger.debug('client asked for -> %r', filename)
        
        # send blocks data to client after compressed 
        with open(filename, 'rb') as input_file:
            while True:
                block = input_file.read(BLOCK_SIZE)
                if not block:
                    break
                self.loggger.debug('RAW -> %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.loggger.debug('SENDING -> %r', binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.loggger.debug('BUFFERING')
        
        # sending data from buffered 
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.loggger.debug('FLUSHING %r', binascii.hexlify(to_send))
            self.request.send(to_send)
        return
    
if __name__ == '__main__':
    import socket
    import threading
    from io import BytesIO
    
    logging.basicConfig(level=logging.DEBUG, format='%(name)s -> %(message)s',)
    logger = logging.getLogger('Client')
    
    # settings server on to one thread
    address = ('localhost', 0)
    server = socketserver.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address
    
    thd = threading.Thread(target=server.serve_forever)
    thd.setDaemon(True)
    thd.start()
    
    # connection to server as a client
    logger.info('Contacting server on %s -> %s', ip, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    # request file 
    requested_file = 'lorem.txt'
    logger.debug('sending filename -> %r', requested_file)
    len_sent = sock.send(requested_file.encode('utf-8'))
    
    # response 
    buffer = BytesIO()
    decompressor = zlib.decompressobj()
    while True:
        response = sock.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ -> %r', binascii.hexlify(response))
        
        # turn on unused data for decompressor 
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOMPRESSED -> %r', decompressed)
                buffer.write(decompressed)
                
                # search data unused for overflow buffer
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('BUFFERING')
                to_decompress  = None
    # data in buffer decompressor 
    remainder = decompressor.flush()
    if remainder:
        logger.debug('FLUSHED -> %r', remainder)
        buffer.write(remainder)
        
    full_response = buffer.getvalue()
    lorem = open('lorem.txt', 'rb').read()
    logger.debug('response matches file contents -> %s', full_response == lorem)
    
    sock.close()
    server.socket.close()