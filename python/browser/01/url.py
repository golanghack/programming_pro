#! /usr/bin/env python3 

import socket

class URL:
    """URl class for request, response and render url"""

    def __init__(self, url: str):
        self.scheme, url = url.split('://', 1)
        assert self.scheme == 'http', f'Unknown scheme -> {self.scheme}'

        # catch path
        if '/' not in url:
            url = url + '/'
        self.host, url = url.split('/', 1)
        self.path = '/' + url

    def request(self):
        """Download page from host""" 

        sock = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP,
        )
        sock.connect((self.host, 80))
        sock.send(('GET % http/1.1\r\n'.format(self.path) + 
                    'Host: %s\r\n\r\n'.format(self.host)).encode('utf8'))
        
        response = sock.makefile('r', encoding='utf8', newline='\r\n')
        statusline = response.readline()
        version, status, explanation = statusline.split(' ', 2)
        assert status == '200', f'{status}: {explanation}'

        headers = {}
        while True:
            line = response.readline()
            if line == '\r\n':
                break
            header, value = line.split(':', 1)
            headers[header.lower()] = value.strip()
        assert 'transfer-encoding' not in headers
        assert 'content-encoding' not in headers

        body = response.read()
        sock.close
        return headers, body

def show(body):
    in_angle = False
    for c in body:
        if c == '<':
            in_angle = True
        elif c == '>':
            in_angle = False
        elif not in_angle:
            print(c, end='')

def load(url):
    headers, body = url.request()
    show(body)

if __name__ == '__main__':
    
    load(URL('http://example.com'))