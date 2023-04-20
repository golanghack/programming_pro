#! /usr/bin/env python3 


import socket

def get_constants(prefix: str) -> dict:
    """Create dict for relation consts from socket module with names."""

    return {
        getattr(socket, n): n 
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('nasa.gov', 'https'):

    # unpacked tuple response
    family, socktype, proto, canonname, sockaddr = response

    print('Family -> ', families[family])
    print('Types -> ', types[socktype])
    print('Protocol -> ', protocols[proto])
    print('Canonical name -> ', canonname)
    print('Socket address -> ', sockaddr)
    print()