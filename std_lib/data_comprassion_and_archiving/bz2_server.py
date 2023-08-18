#! /usr/bin/env python3 

import bz2 
import logging
import socketserver
import binascii

BLOCK_SIZE = 32 

class Bz2RequestHandler(socketserver.BaseRequestHandler):
    
    logger = logging.getLogger('Server')
    
    def handle(self) -> None:
        compressor = bz2.BZ2Compressor()
        
        # file for client
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('client asked for -> "%s"', filename)
        
        # send partial of date after compress
        with open(filename, 'rb') as input_file:
            while True:
                block = input_file.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug('SENDING %r', binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')
                    
        # send data from buffered
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('FLUSHING %r', binascii.hexlify(to_send))
            self.request.send(to_send)
        return
    
    
if __name__ == '__main__':
    import socket
    import sys 
    from io import StringIO
    import threading
    
    logging.basicConfig(level=logging.DEBUG, 
                        format='%(name)s: %(message)s',
                        )
    
    # setting server on only thread
    address = ('localhost', 0) 
    server = socketserver.TCPServer(address, Bz2RequestHandler)
    ip, port = server.server_address
    
    tread = threading.Thread(target=server.serve_forever)
    tread.setDaemon(True)
    tread.start()
    
    logger = logging.getLogger('Client')
    
    # connect to server as a client
    logger.info('Contacting server on %s -> %s', ip, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    # get file 
    requested_file = (sys.argv[0]
                      if len(sys.argv) > 1
                      else 'lorem.txt')
    logger.debug('sending filename -> "%s"', requested_file)
    len_sent = sock.send(requested_file.encode('utf-8'))
    
    # get response
    buffer = StringIO()
    decompressor = bz2.BZ2Decompressor()
    while True:
        response = sock.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))
        
        # include unused data for decompressor
        decompressed = decompressor.decompress(response)
        if decompressed:
            logger.debug('DECOMPRESSED -< %r', decompressed)
            buffer.write(decompressed.decode('utf-8'))
        else:
            logger.debug('BUFFERING')
            
    full_response = buffer.getvalue()
    lorem = open(requested_file, 'rt').read()
    logger.debug('response matches file contents -> %s', full_response == lorem)
    
    # free resourses
    server.shutdown()
    server.socket.close()
    sock.close()
        