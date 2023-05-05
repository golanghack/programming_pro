#! /usr/bin/env python3 

from http.server import BaseHTTPRequestHandler
from urllib import parse

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        message_parts = [
            f'Client values -> {self.client_address} ({self.address_string()})',
            f'command -> {self.command}',
            f'path -> {self.path}',
            f'real path -> {parsed_path.path}',
            f'query -> {parsed_path.query}',
            f'request_version -> {self.request_version}',
            '',
            'Server values -> ',
            f'server_version -> {self.server_version}',
            f'sys_version -> {self.sys_version}',
            f'protocol_version -> {self.protocol_version}',
            '',
            'Headers received -> ',
        ]

        for name, value in sorted(self.headers.items()):
            message_parts.append(
                f'{name} -> {value.rstrip()}'
            )
        
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    from http.server import HTTPServer

    server = HTTPServer(('localhost', 8082), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()