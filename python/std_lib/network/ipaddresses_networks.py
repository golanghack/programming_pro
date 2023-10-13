#! /usr/bin/env python3 

import ipaddress

NETWORKS = [
    '10.9.0.0/24', 
    'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print(f'{net!r}')
    print(' -----is private----- ', net.is_private)
    print(' -----broadcast------ ', net.broadcast_address)
    print(' -----with netmask----- ', net.with_netmask)
    print(' -----compressed----- ', net.compressed)
    print(' -----with hostmask----- ', net.with_hostmask)
    print(' -----num addresses----- ', net.num_addresses)