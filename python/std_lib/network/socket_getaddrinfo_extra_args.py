#! /usr/bin/env python3 

import socket

def get_constants(prefix: str) -> dict:
    """Create dict for relation const from socket module with names."""

    return {
        getattr(socket, n): n 
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

responses = socket.getaddrinfo(host='nasa.gov',
                                 port='https',
                                 family=socket.AF_INET, 
                                 type=socket.SOCK_STREAM, 
                                 proto=socket.IPPROTO_TCP,
                                 flags=socket.AI_CANONNAME,)

for response in responses:
    # unpacked tuple
    family, socktype, proto, canonname, sockaddr = response

    print('Family -> ', families[family])
    print('Type -> ', types[socktype])
    print('Protocol -> ', protocols[proto])
    print('Cannonical name -> ', canonname)
    print('Socket address -> ', sockaddr)
    print()