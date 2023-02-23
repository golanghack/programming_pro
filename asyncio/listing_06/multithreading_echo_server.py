#! /usr/bin/env python3 

from threading import Thread 
import socket

def echo(client: socket) -> None:
    """ECho - elementary function for socket."""
    
    while True:
        data = client.recv(2048) 
        print(f'Got {data}, sending')
        client.sendall(data)
        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    
    while True:
        # blocking until connection
        conn, _ = server.accept()
        # when connection create -> connect client, create Thread
        thread = Thread(target=echo, args=(conn, ))
        thread.start()