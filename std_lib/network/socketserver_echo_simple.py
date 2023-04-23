#! /usr/bin/env python3 

import socketserver

class EchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # message 
        data = self.request.recv(1024)
        self.request.send(data)
        return 

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # connect 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send 
    message = 'Hello'.encode()
    print(f'Sending -> {message!r}')
    len_sent = s.send(message)

    # response 
    response = s.recv(len_sent)
    print(f'Received -> {response!r}')

    # clean 
    server.shutdown()
    s.close()
    server.socket.close()

    