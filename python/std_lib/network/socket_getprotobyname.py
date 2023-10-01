#! /usr/bin/env python3 

import socket

def get_constants(prefix: str) -> dict:
    """Create dict for const from socket module with names."""

    return {
        getattr(socket, n): n 
        for n in dir(socket)
        if n.startswith(prefix)
    }

protocols = get_constants('IPPROTO_')

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print(f'{name:>4} -> {proto_num:2d} (socket.{getattr(socket,const_name):>12})')