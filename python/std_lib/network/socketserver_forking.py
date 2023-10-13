#! /usr/bin/env python3 

import os 
import socketserver

class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # message
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d -> %s' % (cur_pid, data)
        self.request.send(response)
        return

class ForkingEchoServer(socketserver.ForkingMixIn, socketserver.TCPServer):

    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print('Server loop running in process -> ', os.getpid())

    # connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send data 
    message = 'Hello'.encode()
    print(f'Sending -> {message!r}')
    len_senf = s.send(message)

    # response 
    response = s.recv(1024)
    print(f'Received -> {response!r}')

    # clean 
    server.shutdown()
    s.close()
    server.socket.close()