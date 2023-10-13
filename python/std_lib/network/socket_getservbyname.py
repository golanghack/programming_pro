#! /usr/bin/env python3 

import socket
from urllib.parse import urlparse

URLS = [
    'http://python.org', 
    'https://mybank.com', 
    'ftp://prep.ai.mit.edu', 
    'gother://gother.micro.umn.edu', 
    'smtp://mail.example.com',
    'imap://mail.example.com',
    'imaps://mail.example.com', 
    'pop3://pop.exapmle.com',
    'pop3s://pop.example.com',
]

for url in URLS:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print(f'{parsed_url.scheme:>6} -> {port}')