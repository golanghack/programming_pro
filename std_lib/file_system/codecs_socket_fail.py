#! /usr/bin/env python3 

import sys 
import socketserver

class Echo(socketserver.BaseRequestHandler):
    
    def handle(self):
        # get bytes end return client
        data = self.request.recv(1024)
        self.request.send(data)
        return 
    
if __name__ == '__main__':
    import codecs
    import socket
    import threading
    
    # core for address set
    address = ('localhost', 0)
    server = socketserver.TCPServer(address, Echo)
    
    # port
    ip, port = server.server_address
    
    thread = threading.Thread(target=server.serve_forever)
    # from thread to therad Deamon
    thread.setDaemon(True)
    thread.start()
    
    # server connecting
    connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect.connect((ip, port))
    
    # send data
    # DONT! ERROR! NOT ENCODED FIRST
    text = 'Français'
    len_sent = connect.send(text)
    
    # get response
    response = connect.recv(len_sent)
    print(repr(response))
    
    # delete
    connect.close()
    server.socket.close()