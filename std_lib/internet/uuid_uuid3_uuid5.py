#! /usr/bin/env python3 

import uuid

hostnames = ['nasa.gov', 'python.org']

for name in hostnames:
    print(name)
    print(f'MD5 -> {uuid.uuid3(uuid.NAMESPACE_DNS, name)}')
    print(f'SHA1 -> {uuid.uuid5(uuid.NAMESPACE_DNS, name)}')
    print()