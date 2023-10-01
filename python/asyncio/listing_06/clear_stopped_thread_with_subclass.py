#! /usr/bin/env python3 

from threading import Thread 
import socket


class ClientEchoThread(Thread):
    """Custom class for clear stopped echo server threads."""
    
    def __init__(self, client: socket) -> None:
        super().__init__()
        self.client = client
        
    def run(self) -> None:
        """Function for custom running thead."""
        
        try:
            while True:
                data = self.client.recv(2048)
                # if data is empty raise exception
                if not data:
                    raise BrokenPipeError('Connection Close')
                print(f'Gor {data}, sending')
                self.client.sendall(data)
        except OSError as err:
            # exit method run
            print(f'Thead brake exception {err}, stopped.')
            
    def close(self) -> None:
        """Custom closer."""
        
        # breaking connection if thead not activity
        if self.is_alive():
            self.client.sendall(bytes('Stopped...', encoding='utf-8'))
            # stop read and write
            self.client.shutdown(socket.SHUT_RDWR)
            
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    connection_threads = []
    
    try:
        while True:
            connection, address = server.accept()
            thread = ClientEchoThread(connection)
            connection_threads.append(thread)
            thread.start()
        
    except KeyboardInterrupt:
        print('Stopped')
        # call close method for all threads  with Cntrl-C
        [thread.close() for thread in connection_threads]