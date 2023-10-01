#! /usr/bin/env python3 

import socket
import struct
import sys 

message = b'very important data'
multicast_group = ('224.3.29.71', 10000)


# cresate socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# timeout for infinity locking socket 
sock.settimeout(.2)

# set for messages ttl on 1 for limit local network
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    # send multicast group
    print(f'sending {message!r}')
    sent = sock.sendto(message, multicast_group)

    # wait responses from all 
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(64)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print(f'received {data!r} from {server}')

finally:
    print('closing socket')
    sock.close()