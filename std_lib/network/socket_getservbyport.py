#! /usr/bin/env python3 

import socket
from urllib.parse import urlparse

for port in [80, 443, 21, 70, 143, 25, 993, 110, 995]:
    url = f'{socket.getservbyport(port)}://example.com/'
    print(url)