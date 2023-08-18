#! /usr/bin/env python3 

import ipaddress 

ADDRESSES = [
    '10.9.0.0/24', 
    'fdfd:87b5:b475:5e3e::/64',
]

for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print(f'{iface!r}')
    print('network -> \n ', iface.network)
    print('ip -> \n ', iface.ip)
    print('IP with prefixlen -> \n ', iface.with_prefixlen)
    print('netmask -> \n ', iface.with_netmask)
    print('hostmask -> \n ', iface.with_hostmask)
    print()