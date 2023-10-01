#! /usr/bin/env python3 

import ipaddress

NETWORKS = [
    '10.9.0.0/24', 
    'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print(f'{net!r}')
    for i, ip in zip(range(3), net.hosts()):
        print(ip)
    print()