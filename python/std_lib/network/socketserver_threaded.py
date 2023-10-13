#! /usr/bin/env python3 

import threading
import socketserver

class ThreadedEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # message 
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = b'%s -> %s' % (cur_thread.getName().encode(), data)
        self.request.send(response)
        return

class ThreadedEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    pass

if __name__ == '__main__':
    import socket

    address = ('localhost', 0)
    server = ThreadedEchoServer(address, ThreadedEchoRequestHandler)

    ip, port = server.server_address
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print(f'Server loop running in thread -> {t.getName()}')

    # connect 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send 
    message = b'Hello'
    print(f'Sending -> {message!r}')
    len_sent = s.send(message)

    # response 
    response = s.recv(1024)
    print(f'Received -> {response!r}')

    # clean 
    server.shutdown()
    s.close()
    server.socket.close()

